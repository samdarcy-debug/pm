#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub CLI Installation Script

Cross-platform script to automatically install the GitHub CLI (gh) if not present.
Supports Windows (winget), macOS (brew), and Linux (apt).

Exit codes:
  0 - Success (gh CLI installed or already present)
  1 - Installation failed
  2 - Platform not supported or package manager not available
"""

import os
import platform
import subprocess
import sys

# Ensure UTF-8 encoding on Windows
if platform.system() == "Windows":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def run_command(cmd, shell=False, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            capture_output=True,
            text=True,
            check=check
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout.strip() if e.stdout else "", e.stderr.strip() if e.stderr else ""
    except FileNotFoundError:
        return 127, "", f"Command not found: {cmd[0] if isinstance(cmd, list) else cmd}"


def is_gh_installed():
    """Check if gh CLI is already installed."""
    # On Windows, check common installation paths first
    if platform.system() == "Windows":
        common_paths = [
            r"C:\Program Files\GitHub CLI\gh.exe",
            os.path.expanduser(r"~\AppData\Local\Programs\GitHub CLI\gh.exe")
        ]

        for gh_path in common_paths:
            if os.path.exists(gh_path):
                returncode, version, _ = run_command([gh_path, "--version"], check=False)
                if returncode == 0:
                    print(f"✓ GitHub CLI is already installed: {version.split()[2] if len(version.split()) > 2 else 'version unknown'}")
                    return True

        # Fallback to PATH check
        returncode, stdout, _ = run_command(["where", "gh"], check=False)
    else:
        returncode, stdout, _ = run_command(["which", "gh"], check=False)

    if returncode == 0 and stdout:
        # Verify it actually works
        returncode, version, _ = run_command(["gh", "--version"], check=False)
        if returncode == 0:
            print(f"✓ GitHub CLI is already installed: {version.split()[2] if len(version.split()) > 2 else 'version unknown'}")
            return True

    return False


def install_windows():
    """Install gh CLI on Windows using winget."""
    print("📦 Installing GitHub CLI on Windows using winget...")

    # Check if winget is available
    returncode, _, stderr = run_command(["winget", "--version"], check=False)
    if returncode != 0:
        print("❌ winget is not available. winget requires Windows 10 (build 1809+) or Windows 11.")
        print("\n📖 Manual installation options:")
        print("1. Install from: https://cli.github.com/")
        print("2. Or use: scoop install gh")
        print("3. Or use: choco install gh")
        return False

    # Install using winget
    print("Running: winget install --id GitHub.cli...")
    returncode, stdout, stderr = run_command(
        ["winget", "install", "--id", "GitHub.cli", "-e", "--source", "winget"],
        check=False
    )

    if returncode == 0:
        print("✓ GitHub CLI installed successfully!")
        return True
    else:
        print(f"❌ Installation failed: {stderr}")
        if "requires administrator privileges" in stderr.lower() or "requires elevation" in stderr.lower():
            print("\n⚠️  Administrator privileges required.")
            print("Please run this command in an elevated PowerShell/Command Prompt:")
            print("  winget install --id GitHub.cli")
        return False


def install_macos():
    """Install gh CLI on macOS using Homebrew."""
    print("📦 Installing GitHub CLI on macOS using Homebrew...")

    # Check if brew is available
    returncode, _, _ = run_command(["which", "brew"], check=False)
    if returncode != 0:
        print("❌ Homebrew is not installed.")
        print("\n📖 To install Homebrew, run:")
        print('  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        print("\nThen run this script again.")
        return False

    # Install using brew
    print("Running: brew install gh...")
    returncode, stdout, stderr = run_command(["brew", "install", "gh"], check=False)

    if returncode == 0:
        print("✓ GitHub CLI installed successfully!")
        return True
    else:
        print(f"❌ Installation failed: {stderr}")
        return False


def install_linux():
    """Install gh CLI on Linux using apt."""
    print("📦 Installing GitHub CLI on Linux using apt...")

    # Check if we're on a Debian/Ubuntu-based system
    returncode, _, _ = run_command(["which", "apt"], check=False)
    if returncode != 0:
        print("❌ apt package manager not found.")
        print("\n📖 For other Linux distributions, see:")
        print("  https://github.com/cli/cli/blob/trunk/docs/install_linux.md")
        return False

    # Add GitHub CLI repository
    print("Adding GitHub CLI repository...")
    commands = [
        ["sudo", "apt", "update"],
        ["sudo", "apt", "install", "-y", "curl"],
        ["sudo", "mkdir", "-p", "/etc/apt/keyrings"],
        "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/keyrings/githubcli-archive-keyring.gpg",
        "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null",
        ["sudo", "apt", "update"],
        ["sudo", "apt", "install", "-y", "gh"]
    ]

    for cmd in commands:
        if isinstance(cmd, str):
            returncode, _, stderr = run_command(cmd, shell=True, check=False)
        else:
            returncode, _, stderr = run_command(cmd, check=False)

        if returncode != 0:
            print(f"❌ Command failed: {cmd}")
            print(f"Error: {stderr}")
            if "permission denied" in stderr.lower() or "are you root" in stderr.lower():
                print("\n⚠️  This script requires sudo privileges to install packages.")
            return False

    print("✓ GitHub CLI installed successfully!")
    return True


def main():
    """Main installation logic."""
    print("GitHub CLI Installation Script")
    print("=" * 50)

    # Check if already installed
    if is_gh_installed():
        print("\n✓ No installation needed.")
        return 0

    print("\n📍 GitHub CLI not found. Installing...")

    # Detect platform and install
    system = platform.system()
    success = False

    if system == "Windows":
        success = install_windows()
    elif system == "Darwin":
        success = install_macos()
    elif system == "Linux":
        success = install_linux()
    else:
        print(f"❌ Unsupported platform: {system}")
        print("\n📖 Please install GitHub CLI manually from:")
        print("  https://cli.github.com/")
        return 2

    if not success:
        print("\n❌ Installation failed. Please install GitHub CLI manually from:")
        print("  https://cli.github.com/")
        return 1

    # Verify installation
    print("\n🔍 Verifying installation...")
    if is_gh_installed():
        print("\n✅ GitHub CLI is ready to use!")
        print("\n📖 Next step: Authenticate with GitHub")
        print("  Run: gh auth login")
        return 0
    else:
        print("\n⚠️  Installation completed but gh CLI is not in PATH.")
        print("You may need to restart your terminal or add gh to your PATH manually.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
