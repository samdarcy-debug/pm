# Base Template

This template defines the universal frontmatter schema that all documents in this repository must include.

## Required Frontmatter Fields

All documents must include these fields in their YAML frontmatter:

```yaml
---
title:                      # Required. Human-readable title
type:                       # Required. One of: prd | one-pager | rfc | six-pager | person | team | knowledge
status:                     # Required. One of: draft | review | approved | archived
team:                       # Required for team docs. Team slug (e.g., "intelligence")
owner:                      # Required. Wiki-link to person (e.g., "[[people/adam-schoenfeld]]")
created:                    # Required. ISO 8601 date (YYYY-MM-DD)
updated:                    # Required. ISO 8601 date (YYYY-MM-DD)
tags: []                    # Optional. List of tags for discovery
related: []                 # Optional. List of related doc IDs
---
```

## Notes

- **type**: Determines which template conventions apply
- **status**: Reflects the lifecycle state of the document
- **team**: Use the team slug (folder name), not the full team name
- **owner**: The primary person responsible for this document. Use wiki-link format.
- **created/updated**: Use ISO 8601 date format (YYYY-MM-DD)
- **tags**: Free-form but prefer lowercase, hyphenated slugs
- **related**: Reference other documents by their `id` field
