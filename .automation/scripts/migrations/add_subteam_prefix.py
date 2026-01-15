#!/usr/bin/env python3
"""
Add [subteam]- prefix to all sub-team folders in hierarchical teams.
Uses git mv to preserve history.
"""

import subprocess
import sys
from pathlib import Path

# All sub-team folders to rename (16 total across 4 hierarchical teams)
FOLDERS_TO_RENAME = [
    # Intelligence team (4 sub-teams)
    "teams/intelligence/context-engineering",
    "teams/intelligence/mcp",
    "teams/intelligence/semantic-data",
    "teams/intelligence/intelligence-executive-team",

    # Platform team (5 sub-teams)
    "teams/platform/admin",
    "teams/platform/automation",
    "teams/platform/data-platform",
    "teams/platform/integrations",
    "teams/platform/zim",

    # Data team (2 sub-teams)
    "teams/data/core-data",
    "teams/data/data-executive-team",

    # Ops team (3 sub-teams)
    "teams/ops/business-intelligence",
    "teams/ops/product-marketing",
    "teams/ops/product-ops",
]

def add_subteam_prefix(old_path: str) -> str:
    """Add [subteam]- prefix to folder name."""
    path_obj = Path(old_path)
    folder_name = path_obj.name
    new_folder_name = f"[subteam]-{folder_name}"
    new_path = str(path_obj.parent / new_folder_name)
    return new_path

def git_mv(old_path: str, new_path: str, dry_run: bool = False) -> bool:
    """Execute git mv command."""
    if dry_run:
        print(f"[DRY RUN] Would rename: {old_path} -> {new_path}")
        return True

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
    import argparse

    parser = argparse.ArgumentParser(
        description="Add [subteam]- prefix to all sub-team folders"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be renamed without making changes"
    )

    args = parser.parse_args()

    if args.dry_run:
        print("DRY RUN MODE - No changes will be made\n")
    else:
        print("Adding [subteam]- prefix to all sub-team folders...\n")

    success_count = 0
    fail_count = 0
    skip_count = 0

    for old_path in FOLDERS_TO_RENAME:
        if not Path(old_path).exists():
            print(f"[SKIP] Folder not found: {old_path}")
            skip_count += 1
            continue

        new_path = add_subteam_prefix(old_path)

        if Path(new_path).exists():
            print(f"[SKIP] Target already exists: {new_path}")
            skip_count += 1
            continue

        if git_mv(old_path, new_path, dry_run=args.dry_run):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"Summary: {success_count} renamed, {skip_count} skipped, {fail_count} failed")
    print(f"{'='*60}")

    if args.dry_run:
        print("\nRun without --dry-run to apply changes")

    if fail_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
