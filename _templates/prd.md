---
id:                         # Format: prd-{YYYY}-{NNN} (e.g., "prd-2025-001")
title:
type: prd
status: draft               # draft | review | approved | archived
team:
owner:                      # Wiki-link to person (e.g., "[[people/adam-schoenfeld]]")
created:
updated:
tags: []
related: []

# PRD-specific fields
target_ship:                # Target quarter or date (e.g., "Q2 2025" or "2025-06-15")
stakeholders: []            # List of wiki-links to people involved
problem_statement:          # One-line summary of the problem this solves
---

# {Title}

## TL;DR

2-3 sentences summarizing what this PRD proposes and why it matters.

## Problem

**What problem are we solving?**

Describe the user pain point or business need in detail.

**For whom?**

Who experiences this problem? What personas or segments?

**Why now?**

Why is this the right time to solve this? What's the urgency or opportunity?

## Proposed Solution

High-level description of what we're building. Include:

- Core functionality
- User experience at a high level
- Key workflows or use cases

## Success Metrics

How will we know this worked? What metrics will we track?

- **Primary metric**: (e.g., "Increase activation rate by 15%")
- **Secondary metrics**: (e.g., "Reduce support tickets by 20%")
- **Leading indicators**: (e.g., "Feature adoption within first week")

## Scope

### In Scope

What are we building in this iteration? Be specific about features and functionality.

- Feature 1
- Feature 2
- Feature 3

### Out of Scope

What are we explicitly NOT doing? Call out things people might assume are included.

- Feature A (deferred to future iteration)
- Feature B (not solving this problem space yet)

## User Stories

Key user workflows or scenarios this feature enables:

1. **As a [persona], I want to [action] so that [benefit]**
   - Acceptance criteria

2. **As a [persona], I want to [action] so that [benefit]**
   - Acceptance criteria

## Design & Specs

Link to design mocks, technical specs, or architecture docs:

- [Design mockups](#)
- [Technical RFC](link-to-rfc)
- [API specifications](#)

## Dependencies

What needs to be true for this to ship? Dependencies on other teams, systems, or initiatives?

- Dependency 1
- Dependency 2

## Risks & Mitigations

What could go wrong? How do we address it?

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Risk description | High/Med/Low | High/Med/Low | How we'll handle it |

## Open Questions

- [ ] Question 1 that needs answering
- [ ] Question 2 that needs resolution
- [ ] Question 3 requiring input from stakeholders

## Timeline & Milestones

High-level phasing or milestones (if applicable):

- **Phase 1** (Date range): What ships
- **Phase 2** (Date range): What ships
- **Launch** (Target date): Full release

## Approvals

Document key decision points and approvals:

- [ ] Design review completed (Date, Reviewer)
- [ ] Technical review completed (Date, Reviewer)
- [ ] Stakeholder signoff (Date, Stakeholders)
- [ ] Final approval to build (Date, Approver)
