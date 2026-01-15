#!/bin/bash

# Agent PRD Quality Check Script
# Evaluates an Agent PRD against quality criteria using LLM-as-judge
# Usage: ./quality-check.sh [path-to-prd.md]

set -euo pipefail

PRD_FILE="${1:-}"

if [[ -z "$PRD_FILE" ]]; then
  echo "Usage: ./quality-check.sh [path-to-prd.md]"
  exit 1
fi

if [[ ! -f "$PRD_FILE" ]]; then
  echo "Error: File not found: $PRD_FILE"
  exit 1
fi

echo "📊 Agent PRD Quality Assessment"
echo ""
echo "Analyzing: $PRD_FILE"
echo ""
echo "This script uses Claude to evaluate your Agent PRD against best practices."
echo "It will score each of the 13 sections and provide improvement recommendations."
echo ""
echo "⚠️  Implementation Note: This script is designed to be called from within"
echo "    Claude Code, which will handle the LLM evaluation logic."
echo ""
echo "To use this script:"
echo "1. Open Claude Code in this repository"
echo "2. Say: 'Run quality check on [path-to-prd.md]'"
echo "3. Claude will evaluate each section and provide detailed scores"
echo ""
echo "The evaluation will check:"
echo "  • Section 1: Job to Be Done (target: 90+)"
echo "  • Section 2: Scope & Decomposition (target: 90+)"
echo "  • Section 3: Opaque Executor Contract (target: 90+)"
echo "  • Section 4: Context Requirements (target: 90+)"
echo "  • Section 5: Ideal Flow (target: 90+)"
echo "  • Section 6: Test Cases (target: 90+)"
echo "  • Section 7: Dependencies (target: 90+)"
echo "  • Section 8: Prompt Structure (target: 90+)"
echo "  • Section 9: Human-in-the-Loop Design (target: 90+)"
echo "  • Section 10: Metrics (target: 90+)"
echo "  • Section 11: Data Flywheel (target: 90+)"
echo "  • Section 12: Competitive Comparative (target: 90+)"
echo "  • Section 13: Rollout & Communication (target: 90+)"
echo ""
echo "Quality criteria reference:"
echo "  .claude/skills/agent-prd/references/quality-criteria.md"
