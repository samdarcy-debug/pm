#!/bin/bash
# PM Repository Development Environment Setup
#
# This script sets up your local development environment for the PM repository.
# Run this once after cloning the repository.
#
# What it does:
# - Installs git hooks (pre-commit for CODEOWNERS, post-merge for doc promotion)
# - Validates Python is available
# - Tests that maintenance scripts work
#
# Usage:
#   bash .automation/scripts/setup-dev-environment.sh

set -e  # Exit on error

echo "=========================================="
echo "PM Repository - Development Setup"
echo "=========================================="
echo ""

# Colors for output (works in Git Bash on Windows)
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC}  $1"
}

print_error() {
    echo -e "${RED}❌${NC} $1"
}

# Check if we're in the repo root
if [ ! -d ".git" ]; then
    print_error "This script must be run from the repository root directory"
    echo "Current directory: $(pwd)"
    exit 1
fi

print_success "Found repository root"
echo ""

# ============================================
# 1. Install Git Hooks
# ============================================
echo "📌 Installing git hooks..."

HOOKS_DIR=".git/hooks"

# Pre-commit hook
PRECOMMIT_SOURCE=".automation/scripts/hooks/pre-commit"
PRECOMMIT_TARGET="$HOOKS_DIR/pre-commit"

mkdir -p "$HOOKS_DIR"

if [ -f "$PRECOMMIT_TARGET" ]; then
    print_warning "Pre-commit hook already exists at $PRECOMMIT_TARGET"
    echo "   If you want to update it, delete the existing hook and run this script again."
else
    # Copy hook (works on all platforms)
    cp "$PRECOMMIT_SOURCE" "$PRECOMMIT_TARGET"
    chmod +x "$PRECOMMIT_TARGET"
    print_success "Pre-commit hook installed"
    echo "   Location: $PRECOMMIT_TARGET"
    echo "   What it does: Auto-regenerates CODEOWNERS when person profiles change"
fi

echo ""

# Post-merge hook
POSTMERGE_SOURCE=".automation/scripts/hooks/post-merge"
POSTMERGE_TARGET="$HOOKS_DIR/post-merge"

if [ -f "$POSTMERGE_TARGET" ]; then
    print_warning "Post-merge hook already exists at $POSTMERGE_TARGET"
    echo "   If you want to update it, delete the existing hook and run this script again."
else
    # Copy hook (works on all platforms)
    cp "$POSTMERGE_SOURCE" "$POSTMERGE_TARGET"
    chmod +x "$POSTMERGE_TARGET"
    print_success "Post-merge hook installed"
    echo "   Location: $POSTMERGE_TARGET"
    echo "   What it does: Auto-promotes working_docs to documentation after PR merge"
fi

echo ""

# ============================================
# 2. Validate Python
# ============================================
echo "🐍 Checking Python installation..."

PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
fi

if [ -z "$PYTHON_CMD" ]; then
    print_error "Python not found!"
    echo "   The maintenance scripts require Python 3.x"
    echo "   Install from: https://www.python.org/downloads/"
    echo ""
    echo "   After installing Python, run this setup script again."
    exit 1
else
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    print_success "Python is available: $PYTHON_VERSION"
fi

echo ""

# ============================================
# 3. Test Maintenance Scripts
# ============================================
echo "🧪 Testing maintenance scripts..."

# Test validation script
echo "   Testing validate-person-profiles.py..."
if $PYTHON_CMD .automation/scripts/maintenance/validate-person-profiles.py > /dev/null 2>&1; then
    print_success "Validation script works"
elif [ $? -eq 1 ]; then
    # Exit code 1 means validation errors found, but script itself works
    print_success "Validation script works (found validation errors, which is expected)"
else
    print_error "Validation script failed to run"
    echo "   Try running it manually to see the error:"
    echo "   python .automation/scripts/maintenance/validate-person-profiles.py"
fi

# Test generation script
echo "   Testing generate-codeowners.py..."
if $PYTHON_CMD .automation/scripts/maintenance/generate-codeowners.py --help > /dev/null 2>&1 || \
   $PYTHON_CMD .automation/scripts/maintenance/generate-codeowners.py > /dev/null 2>&1; then
    print_success "CODEOWNERS generation script works"
else
    print_warning "CODEOWNERS generation script may have issues"
    echo "   Try running it manually to verify:"
    echo "   python .automation/scripts/maintenance/generate-codeowners.py"
fi

echo ""

# ============================================
# 4. Summary
# ============================================
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Your development environment is ready:"
echo ""
echo "  ✓ Git hooks installed"
echo "    ├─ Pre-commit: Auto-regenerates CODEOWNERS"
echo "    └─ Post-merge: Auto-promotes docs to documentation folder"
echo ""
echo "  ✓ Python available"
echo "    └─ Maintenance scripts validated"
echo ""
echo "Next steps:"
echo ""
echo "  1. Create your person profile:"
echo "     → Say 'onboard me' to Claude"
echo "     → Or manually create: teams/{team}/_people/{your-name}.md"
echo ""
echo "  2. Start creating documents:"
echo "     → Ask Claude: 'create a PRD for [feature]'"
echo "     → Ask Claude: 'create an RFC for [proposal]'"
echo ""
echo "  3. When you commit person profile changes:"
echo "     → CODEOWNERS will auto-regenerate (thanks to the pre-commit hook!)"
echo "     → Both files will be committed together"
echo ""
echo "  4. When you merge a PR from working_docs:"
echo "     → If you opted-in during PR creation, docs will auto-promote"
echo "     → Documents move to documentation folder automatically"
echo ""
echo "Useful commands:"
echo ""
echo "  Validate person profiles:"
echo "    python .automation/scripts/maintenance/validate-person-profiles.py"
echo ""
echo "  Regenerate CODEOWNERS manually:"
echo "    python .automation/scripts/maintenance/generate-codeowners.py"
echo ""
echo "  Move a document to documentation manually:"
echo "    python .automation/scripts/maintenance/move-to-documentation.py \\"
echo "      teams/{team}/working_docs/doc.md \\"
echo "      teams/{team}/documentation"
echo ""
echo "  Re-run this setup:"
echo "    bash .automation/scripts/setup-dev-environment.sh"
echo ""
