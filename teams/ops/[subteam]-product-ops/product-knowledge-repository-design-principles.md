# Product Knowledge Repository - Design Principles

## What This Is

Think of this as Google Drive for the product org - with a product operations oracle built in. You get the best of Google Drive, Github functionality, and Claude Code.

**Like Google Drive:** You create documents, share them with your team, collaborate on them, find old work.

**What makes this different:**

### The Oracle

You're writing alongside an AI that knows YOUR product org specifically - every past PRD, every learning, every decision

- Ask: "Will this work for enterprise persona?" and it references your actual persona docs and past enterprise learnings
- Ask: "Have we tried something like this before?" and it finds the relevant past work and what happened
- It warns you: "Past PRDs about integrations encountered X issue" before you make the same mistake
- This oracle gets smarter over time as you add more knowledge - it learns YOUR org, not generic product management

### Templates + Skills

- Every document type has a template that embodies your best practices
- Skills guide you through creation: "Create a PRD" walks you through the right questions based on what you're building
- The template isn't just structure - it's your org's accumulated wisdom about how to do this well

### Code-Style Collaboration

- Document review works like code review (pull requests, inline comments, change tracking)
- See exactly what changed between versions
- Comments thread to specific lines, decisions are explicit
- Collaboration is structured, not just "someone made changes somewhere"

### It Compounds

- Past work automatically makes future work better
- Learnings get extracted and become part of the oracle's knowledge
- New PMs learn by exploring what came before
- Knowledge doesn't just pile up - it becomes more useful

### The Foundation

- Git provides version control and structured collaboration
- Markdown keeps things simple and portable
- Claude Code (with skills) is the oracle interface
- Structure enables the oracle to actually understand your work

**The key difference:** Google Drive with Gemini is a generic AI that happens to see your docs. This is a specialized oracle that deeply understands YOUR product organization and gets smarter as you work.

## Vision

This repository becomes the "brain" for our product organization:

- Every decision, PRD, learning, and principle lives here
- Claude Code acts as an oracle that knows all of it
- Creating new work automatically benefits from past work
- The system prevents repeating mistakes
- New team members learn by talking to the oracle

We're building a system where a PM can ask "What do we know about integrations?" and get answers specific to OUR products and OUR learnings, where creating a PRD means working alongside an AI that knows every integration we've ever built, and where that AI gets better every time we document something new.

## Core Principles

### Interface & Interaction

#### 1. Natural Language First

- PMs should never type git commands or edit config files
- Every workflow should work through conversational interaction with Claude Code
- "Create a PRD for X" should just work - no memorizing syntax
- The oracle responds to natural questions, not search queries

#### 2. Works for Non-Technical Users

- Assume PM has never used git or command line
- GitHub Desktop handles git operations visually
- Markdown is the only "technical" thing they need to learn (and it's minimal)
- System should teach itself through use
- If a PM needs a manual to use this, we've failed

#### 3. AI is the Interface

- Claude Code is how PMs interact with this repo
- Documentation is written for both humans AND AI to read
- Structure optimized for AI querying and synthesis
- The better Claude Code understands the repo, the better the PM experience
- Skills are the oracle's specialized capabilities

#### 4. Git is the Foundation, Not the Interface

- Git provides: version control, collaboration (PRs), history, backup
- PMs don't need to understand git internals
- They need to understand: create documents, get feedback, find things
- Code-style collaboration without code-style complexity

### Architecture & Evolution

#### 5. Extensible by Design

- We're building in phases - document creation first, then review, then knowledge curation
- Architecture should support future capabilities without rework
- Don't over-engineer today, but don't box yourself in either
- The oracle should get smarter over time, not just accumulate more data

#### 6. Self-Documenting System

- Structure should be intuitive by exploring
- Good examples are better than long manuals
- The oracle explains itself when asked

#### 7. Knowledge Should Compound

- Past work makes future work easier
- Learnings get extracted and reused
- AI helps surface relevant past context automatically
- System gets smarter over time, not just bigger
- The oracle learns from every document added

### Organization & Ownership

#### 8. Team-Based Organization

- Work lives with teams, not in a global pile
- Each team has their own space they control
- Teams can see across to other teams' work (transparency)
- Product Ops curates global/cross-team knowledge
- The oracle understands team boundaries and relationships

#### 9. People Are First-Class Entities

- Every person in the system has a profile document
- Documents reference people (owner, stakeholders, reviewers)
- AI can answer: "What has Adam been working on?" or "Who owns this?"
- Your identity travels with your work
- The oracle knows who does what

#### 10. Ownership is Clear and Explicit

- Every document has one primary owner
- Owner is in the frontmatter, not just git history
- Ownership can transfer (people change roles, projects hand off)
- When you need feedback on a doc, it's obvious who to ask
- The oracle can route questions to the right people

#### 11. Relationships Are Explicit

- Documents link to other documents
- Documents link to people
- Tags and metadata make things findable
- AI can navigate these relationships to answer questions
- The oracle understands how everything connects

#### 12. Teams Self-Organize

- Teams manage their own folder structure within standard conventions
- Teams decide what goes in documentation vs working_docs
- Product Ops provides the scaffolding, teams fill it in
- No central bottleneck for day-to-day work
- The oracle adapts to how teams actually work

### Implementation Philosophy

#### 14. Optimize for the Experience, Not the Structure

- Prioritize the conversational interaction over file organization
- Make the default path always work (don't make PMs choose)
- When there's a tradeoff between "technically pure" and "easy to use", choose easy
- Every feature should work through natural language first, GUI second, command line never
- The oracle should feel helpful, not technical
