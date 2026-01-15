#!/usr/bin/env python3
"""
Rename weekly reports to new naming convention:
1. synthesis-YYYY-MM-DD.md -> product-executive-report-YYYY-MM-DD.md
2. {team-slug}.md -> {team-slug}-weekly-report-YYYY-MM-DD.md
"""

import os
import subprocess
from pathlib import Path

def rename_synthesis_reports():
    """Rename synthesis reports in weekly-reports/synthesis/"""
    synthesis_dir = Path("weekly-reports/synthesis")

    if not synthesis_dir.exists():
        print(f"Directory not found: {synthesis_dir}")
        return

    renamed_count = 0
    for file in synthesis_dir.glob("synthesis-*.md"):
        new_name = file.name.replace("synthesis-", "product-executive-report-")
        new_path = file.parent / new_name

        # Use git mv to preserve history
        result = subprocess.run(
            ["git", "mv", str(file), str(new_path)],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"Renamed: {file.name} -> {new_name}")
            renamed_count += 1
        else:
            print(f"Failed to rename {file.name}: {result.stderr}")

    print(f"\nSynthesis reports renamed: {renamed_count}")

def rename_team_reports():
    """Rename team reports in weekly-reports/team-reports/YYYY-MM-DD/"""
    team_reports_dir = Path("weekly-reports/team-reports")

    if not team_reports_dir.exists():
        print(f"Directory not found: {team_reports_dir}")
        return

    renamed_count = 0

    # Iterate through date folders
    for date_folder in sorted(team_reports_dir.iterdir()):
        if not date_folder.is_dir():
            continue

        # Extract date from folder name (YYYY-MM-DD)
        date = date_folder.name

        # Process all .md files in this folder
        for file in date_folder.glob("*.md"):
            # Skip files already renamed
            if "-weekly-report-" in file.name:
                continue

            # Extract team slug (filename without .md)
            team_slug = file.stem

            # New filename: {team-slug}-weekly-report-YYYY-MM-DD.md
            new_name = f"{team_slug}-weekly-report-{date}.md"
            new_path = file.parent / new_name

            # Use git mv to preserve history
            result = subprocess.run(
                ["git", "mv", str(file), str(new_path)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"Renamed: {date}/{file.name} -> {new_name}")
                renamed_count += 1
            else:
                print(f"Failed to rename {date}/{file.name}: {result.stderr}")

    print(f"\nTeam reports renamed: {renamed_count}")

if __name__ == "__main__":
    print("=== Renaming Synthesis Reports ===")
    rename_synthesis_reports()

    print("\n=== Renaming Team Reports ===")
    rename_team_reports()

    print("\n=== Done ===")
    print("Review the changes with: git status")
    print("Commit with: git commit -m 'Rename weekly reports to new naming convention'")
