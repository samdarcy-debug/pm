#!/usr/bin/env python3
"""
Rename copilot weekly reports to gtm-workspace from August 2025 onwards.
Uses git mv to preserve history.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Files to rename (from August 1, 2025 onwards)
FILES_TO_RENAME = [
    "weekly-reports/team-reports/2025-08-01/copilot-weekly-report-2025-08-01.md",
    "weekly-reports/team-reports/2025-08-08/copilot-weekly-report-2025-08-08.md",
    "weekly-reports/team-reports/2025-08-15/copilot-weekly-report-2025-08-15.md",
    "weekly-reports/team-reports/2025-08-22/copilot-weekly-report-2025-08-22.md",
    "weekly-reports/team-reports/2025-08-29/copilot-weekly-report-2025-08-29.md",
    "weekly-reports/team-reports/2025-09-06/copilot-weekly-report-2025-09-06.md",
    "weekly-reports/team-reports/2025-09-19/copilot-weekly-report-2025-09-19.md",
    "weekly-reports/team-reports/2025-09-26/copilot-weekly-report-2025-09-26.md",
    "weekly-reports/team-reports/2025-10-03/copilot-weekly-report-2025-10-03.md",
    "weekly-reports/team-reports/2025-10-10/copilot-weekly-report-2025-10-10.md",
    "weekly-reports/team-reports/2025-10-17/copilot-weekly-report-2025-10-17.md",
    "weekly-reports/team-reports/2025-10-24/copilot-weekly-report-2025-10-24.md",
    "weekly-reports/team-reports/2025-10-31/copilot-weekly-report-2025-10-31.md",
    "weekly-reports/team-reports/2025-11-07/copilot-weekly-report-2025-11-07.md",
    "weekly-reports/team-reports/2025-11-14/copilot-weekly-report-2025-11-14.md",
    "weekly-reports/team-reports/2025-12-19/copilot-weekly-report-2025-12-19.md",
]

def rename_file(old_path: str) -> str:
    """Rename copilot to gtm-workspace in filename."""
    new_path = old_path.replace("copilot-weekly-report", "gtm-workspace-weekly-report")
    return new_path

def git_mv(old_path: str, new_path: str) -> bool:
    """Execute git mv command."""
    try:
        result = subprocess.run(
            ["git", "mv", old_path, new_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"[OK] Renamed: {old_path} -> {new_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error renaming {old_path}: {e.stderr}")
        return False

def main():
    print("Renaming copilot reports to gtm-workspace (August 2025 onwards)...\n")

    success_count = 0
    fail_count = 0

    for old_path in FILES_TO_RENAME:
        if not Path(old_path).exists():
            print(f"[WARNING] File not found: {old_path}")
            fail_count += 1
            continue

        new_path = rename_file(old_path)

        if git_mv(old_path, new_path):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"Summary: {success_count} renamed, {fail_count} failed")
    print(f"{'='*60}")

    if fail_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
