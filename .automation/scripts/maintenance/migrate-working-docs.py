#!/usr/bin/env python3
"""
Migrate working_docs folders to new PR-based structure.

This script:
1. Scans all teams/*/working_docs/ folders (including hierarchical teams)
2. Determines destination based on content structure
3. Moves files preserving git history (git mv)
4. Updates frontmatter 'updated' field to migration date
5. Generates migration report showing all moves

Usage:
    # Dry run (review proposed moves)
    python migrate-working-docs.py --dry-run

    # Migrate specific team
    python migrate-working-docs.py --team intelligence

    # Migrate all teams
    python migrate-working-docs.py --all

    # Migrate all and auto-commit per team
    python migrate-working-docs.py --all --commit
"""

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple


def parse_frontmatter(content: str) -> Tuple[Dict, str, str]:
    """Extract YAML frontmatter from markdown content.

    Returns:
        tuple: (frontmatter_dict, frontmatter_text, content_after_frontmatter)
    """
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}, None, content

    frontmatter_text = match.group(1)
    content_after = match.group(2)
    frontmatter = {}

    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes and comments
            value = re.sub(r'#.*$', '', value).strip()
            value = value.strip('"\'')
            if value:
                frontmatter[key] = value

    return frontmatter, frontmatter_text, content_after


def update_frontmatter(content: str, updates: Dict[str, str]) -> str:
    """Update specific frontmatter fields while preserving structure.

    Args:
        content: Original markdown content with frontmatter
        updates: Dict of fields to update (e.g., {'updated': '2026-01-13'})

    Returns:
        str: Updated markdown content
    """
    frontmatter, frontmatter_text, content_after = parse_frontmatter(content)

    if not frontmatter_text:
        # No frontmatter, return original content
        return content

    # Update the frontmatter dict
    for key, value in updates.items():
        frontmatter[key] = value

    # Rebuild frontmatter text, preserving order where possible
    lines = frontmatter_text.split('\n')
    updated_lines = []
    updated_keys = set()

    for line in lines:
        if ':' in line:
            key = line.split(':', 1)[0].strip()
            if key in updates:
                # Update this line with new value
                updated_lines.append(f"{key}: {updates[key]}")
                updated_keys.add(key)
            else:
                # Keep original line
                updated_lines.append(line)
        else:
            # Keep non-key lines (comments, blank lines)
            updated_lines.append(line)

    # Add any new keys that weren't in original frontmatter
    for key, value in updates.items():
        if key not in updated_keys:
            updated_lines.append(f"{key}: {value}")

    # Rebuild full content
    updated_frontmatter_text = '\n'.join(updated_lines)
    return f"---\n{updated_frontmatter_text}\n---\n{content_after}"


def get_repo_root() -> Path:
    """Get repository root path."""
    try:
        repo_root = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            encoding='utf-8'
        ).strip()
        return Path(repo_root)
    except subprocess.CalledProcessError:
        print("[ERROR] Not in a git repository")
        sys.exit(1)


def find_working_docs_folders(repo_root: Path) -> List[Path]:
    """Find all working_docs folders in teams/ directory."""
    teams_dir = repo_root / 'teams'
    working_docs_folders = []

    for path in teams_dir.rglob('working_docs'):
        if path.is_dir():
            working_docs_folders.append(path)

    return sorted(working_docs_folders)


def determine_destination(working_docs_path: Path) -> Dict[str, Path]:
    """Determine destination for contents of working_docs folder.

    Returns:
        Dict mapping source paths to destination paths
    """
    moves = {}

    # Get team folder (parent of working_docs)
    team_folder = working_docs_path.parent

    # Check if working_docs has type-based subfolders
    type_folders = ['prds', 'rfcs', 'one-pagers', 'six-pagers', 'documentation']
    has_type_folders = any((working_docs_path / folder).exists() for folder in type_folders)

    if has_type_folders:
        # Move each type folder up to team level
        for type_folder in type_folders:
            source_dir = working_docs_path / type_folder
            if source_dir.exists() and source_dir.is_dir():
                dest_dir = team_folder / type_folder

                # Find all files in this type folder
                for file in source_dir.rglob('*.md'):
                    if file.is_file():
                        relative_path = file.relative_to(source_dir)
                        dest_file = dest_dir / relative_path
                        moves[file] = dest_file
    else:
        # Flat structure - move files to appropriate subfolder or team root
        # Check if there's already a documentation folder at team level
        team_docs_folder = team_folder / 'documentation'

        for file in working_docs_path.rglob('*.md'):
            if file.is_file():
                # Move to team documentation folder
                if not team_docs_folder.exists():
                    team_docs_folder = team_folder / 'docs'

                relative_path = file.relative_to(working_docs_path)
                dest_file = team_docs_folder / relative_path
                moves[file] = dest_file

    return moves


def execute_move(source: Path, dest: Path, repo_root: Path, dry_run: bool = False) -> bool:
    """Execute a single file move using git mv.

    Args:
        source: Source file path
        dest: Destination file path
        repo_root: Repository root
        dry_run: If True, only print what would be done

    Returns:
        bool: True if successful
    """
    if dry_run:
        print(f"  [DRY RUN] {source.relative_to(repo_root)} -> {dest.relative_to(repo_root)}")
        return True

    try:
        # Read and update frontmatter
        with open(source, 'r', encoding='utf-8') as f:
            content = f.read()

        today = date.today().strftime('%Y-%m-%d')
        updated_content = update_frontmatter(content, {'updated': today})

        # Create destination directory
        dest.parent.mkdir(parents=True, exist_ok=True)

        # Write to destination first
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        # Git add destination, git rm source
        subprocess.run(['git', 'add', str(dest)],
                      cwd=repo_root, check=True, capture_output=True)
        subprocess.run(['git', 'rm', str(source)],
                      cwd=repo_root, check=True, capture_output=True)

        print(f"  * {source.relative_to(repo_root)} -> {dest.relative_to(repo_root)}")
        return True

    except Exception as e:
        print(f"  X Failed to move {source.relative_to(repo_root)}: {e}")
        return False


def get_team_name(working_docs_path: Path, repo_root: Path) -> str:
    """Extract team name from working_docs path."""
    relative = working_docs_path.relative_to(repo_root / 'teams')
    parts = relative.parts

    # For hierarchical teams: teams/{dai}/[subteam]-{name}/working_docs
    # Return: {dai}/{name}
    # For flat teams: teams/{team}/working_docs
    # Return: {team}

    if len(parts) == 2:
        # Flat team
        return parts[0]
    elif len(parts) == 3:
        # Hierarchical team
        dai = parts[0]
        subteam = parts[1]
        if subteam.startswith('[subteam]-'):
            subteam = subteam.replace('[subteam]-', '')
        return f"{dai}/{subteam}"
    else:
        return str(relative.parent)


def migrate_team(working_docs_path: Path, repo_root: Path, dry_run: bool = False,
                commit: bool = False) -> Tuple[int, int]:
    """Migrate a single team's working_docs folder.

    Returns:
        Tuple of (success_count, failure_count)
    """
    team_name = get_team_name(working_docs_path, repo_root)
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Migrating team: {team_name}")
    print(f"  Source: {working_docs_path.relative_to(repo_root)}")

    # Determine destinations
    moves = determine_destination(working_docs_path)

    if not moves:
        print("  No files to migrate")
        return 0, 0

    print(f"  Found {len(moves)} file(s) to migrate")

    # Execute moves
    success_count = 0
    failure_count = 0

    for source, dest in moves.items():
        if execute_move(source, dest, repo_root, dry_run):
            success_count += 1
        else:
            failure_count += 1

    # Commit if requested and not dry run
    if commit and not dry_run and success_count > 0:
        commit_message = f"""refactor: migrate {team_name} from working_docs to team folders

Migrated {success_count} document(s) as part of PR-based workflow migration.
All content is now in team-controlled folder structure.

Co-Authored-By: Claude <noreply@anthropic.com>"""

        try:
            subprocess.run(['git', 'commit', '-m', commit_message],
                         cwd=repo_root, check=True, capture_output=True)
            print(f"  * Committed {success_count} file(s)")
        except subprocess.CalledProcessError as e:
            print(f"  X Failed to commit: {e}")

    return success_count, failure_count


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Migrate working_docs folders to PR-based structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--team', help='Migrate specific team (e.g., "intelligence", "ops")')
    group.add_argument('--all', action='store_true', help='Migrate all teams')

    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without actually doing it')
    parser.add_argument('--commit', action='store_true',
                       help='Auto-commit changes per team (only with --all)')

    args = parser.parse_args()

    # Get repository root
    repo_root = get_repo_root()
    print(f"Repository root: {repo_root}")

    # Find all working_docs folders
    all_folders = find_working_docs_folders(repo_root)

    if not all_folders:
        print("\nNo working_docs folders found!")
        sys.exit(0)

    print(f"\nFound {len(all_folders)} working_docs folder(s)")

    # Filter by team if specified
    if args.team:
        filtered = [f for f in all_folders if args.team in str(f)]
        if not filtered:
            print(f"\n[ERROR] No working_docs folders found for team '{args.team}'")
            print("\nAvailable teams:")
            for folder in all_folders:
                print(f"  - {get_team_name(folder, repo_root)}")
            sys.exit(1)
        folders_to_migrate = filtered
    else:
        folders_to_migrate = all_folders

    # Execute migration
    total_success = 0
    total_failure = 0

    for folder in folders_to_migrate:
        success, failure = migrate_team(folder, repo_root, args.dry_run, args.commit)
        total_success += success
        total_failure += failure

    # Summary
    print(f"\n{'='*60}")
    print("Migration Summary")
    print(f"{'='*60}")
    print(f"  Total files migrated: {total_success}")
    if total_failure > 0:
        print(f"  Total failures: {total_failure}")

    if args.dry_run:
        print("\n[DRY RUN] No changes were made")
        print("Run without --dry-run to execute migration")
    elif total_success > 0:
        print("\n* Migration complete!")
        if not args.commit:
            print("  Don't forget to commit your changes:")
            print("  git add -A")
            print('  git commit -m "refactor: migrate working_docs to team folders"')

    sys.exit(0 if total_failure == 0 else 1)


if __name__ == "__main__":
    main()
