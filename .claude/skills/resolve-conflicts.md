---
skill_name: resolve-conflicts
description: Guides users through resolving git merge conflicts conversationally
trigger: When user encounters merge conflict or says "resolve conflicts"
---

# Resolve Conflicts Skill

This skill helps non-technical users resolve git merge conflicts through conversation.

## When to Use

Trigger this skill when:
- User reports a merge conflict error
- User's push fails due to conflicting changes
- You detect conflict markers in files (`<<<<<<<`, `=======`, `>>>>>>>`)
- User asks for help with conflicts

## How It Works

### 1. Detect Conflicts

Check for files with conflicts:
```bash
git status --short | grep '^UU'
```

List all conflicted files for the user.

### 2. Show Each Conflict Conversationally

For each conflicted file:
1. Read the file to find conflict markers
2. Extract the conflicting sections
3. Present them clearly to the user:

```
I found a conflict in teams/ops/working_docs/prds/example.md

Here's what happened:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR VERSION:
Launch date: Q1 2026
Expected revenue: $500K

THEIR VERSION (by Adam, 2 hours ago):
Launch date: Q2 2026
Expected revenue: $750K
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What would you like to do?
1. Keep your version (Q1 2026, $500K)
2. Keep their version (Q2 2026, $750K)
3. Combine both (I'll help you merge them)
4. Show me the full file context
```

### 3. Get User's Decision

Based on their choice:

**Option 1: Keep theirs**
```bash
git checkout --theirs path/to/file.md
git add path/to/file.md
```

**Option 2: Keep yours**
```bash
git checkout --ours path/to/file.md
git add path/to/file.md
```

**Option 3: Combine both**
- Read both versions
- Ask user how to combine them
- Use Edit tool to create merged version
- Stage the resolved file

**Option 4: Show context**
- Show surrounding sections of the file
- Help user understand what each version means
- Return to presenting options 1-3

### 4. Complete Resolution

After all conflicts are resolved:
```bash
git status  # Verify no remaining conflicts
git rebase --continue  # Or git merge --continue
```

Then push:
```bash
git push
```

Confirm success to user: "All conflicts resolved and pushed successfully!"

## Example Conversation Flow

```
User: My push failed with a merge conflict

Claude: I see you have a merge conflict. Let me help resolve it.

[Runs git status to detect conflicts]

Claude: I found 1 conflict in teams/intelligence/working_docs/prds/agent-framework.md

Here's what happened:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR VERSION:
## Timeline
- Phase 1: Q1 2026
- Phase 2: Q2 2026

THEIR VERSION (by Sarah, 30 minutes ago):
## Timeline
- Phase 1: Q2 2026 (adjusted for dependencies)
- Phase 2: Q3 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What would you like to do?
1. Keep your version (Q1/Q2)
2. Keep Sarah's version (Q2/Q3)
3. Combine both versions
4. Show me more context

User: Keep Sarah's version, she probably has better info

Claude: Got it. Keeping Sarah's version.

[Runs: git checkout --theirs teams/intelligence/working_docs/prds/agent-framework.md]
[Runs: git add teams/intelligence/working_docs/prds/agent-framework.md]
[Runs: git rebase --continue]
[Runs: git push]

Claude: ✓ Conflict resolved! Sarah's timeline is now in the document and pushed successfully.
```

## Best Practices

1. **Be clear about what's different**: Don't just show raw diffs, explain what each version says
2. **Show who and when**: Always mention who made the other change and when
3. **Provide context**: If the conflict is small, show surrounding lines to help user decide
4. **Confirm before finalizing**: After resolving, show what the final version looks like
5. **Handle multiple conflicts**: If there are multiple files, do them one at a time
6. **Stay calm**: Conflicts are normal, keep the tone helpful and non-alarming

## Edge Cases

**Multiple conflicts in one file**: Resolve them in order from top to bottom of the file

**Binary files**: Can't merge automatically - ask user which version to keep entirely

**Rebase vs merge conflicts**: The commands differ slightly:
- Rebase: `git rebase --continue` when done
- Merge: `git merge --continue` when done

Check with `git status` to see which operation is in progress.

## Technical Notes

- Always use `git checkout --theirs` or `git checkout --ours` for simple resolutions
- For complex merges, use the Edit tool to manually create the merged version
- Remember to `git add` after resolving each file
- Only call `--continue` after ALL conflicts are resolved
- If user wants to abort: `git rebase --abort` or `git merge --abort`
