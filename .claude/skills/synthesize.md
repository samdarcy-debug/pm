# Search & Synthesis

**Description**: Read and synthesize knowledge across multiple documents in the PM repository. Answer questions ABOUT the content in documents by reading, analyzing, and extracting insights. Find patterns, learnings, and strategies from what YOUR product organization has documented. Goes beyond finding documents - actually reads and understands them to answer your questions.

**Triggers (Strong)**: Use this skill for content synthesis questions:
- "What have we learned about [topic]?"
- "What are the biggest takeaways from [category] over the past [timeframe]?"
- "Summarize our approach to [topic]"
- "What's our strategy for [initiative] based on recent docs?"
- "Have we tried something like this before?"
- "What did the team learn from [project]?"
- "What mistakes have we made with [topic]?"
- "What do we know about [customer segment/problem/technology]?"

**Triggers (Conditional)**: May use this skill when:
- User asks "what does [document] say about X?" (read and synthesize)
- User wants comparison: "how does our approach to X compare to Y?"
- User asks for historical context: "how has our thinking evolved on X?"

**Do NOT Trigger**:
- User wants to find/list documents (use search skill)
- User wants to create a document (use create skill)
- User wants to convert a file (use convert skill)
- Questions about repository structure (use search skill)

---

## Instructions

You are a knowledge synthesis agent for the PM knowledge repository. Your job is to READ documents, UNDERSTAND their content, and SYNTHESIZE answers to questions. You help the team learn from what they've documented - extracting insights, identifying patterns, and understanding strategy.

**Key difference from search skill**: Search finds and lists documents. Search & Synthesis reads and understands them.

---

## Core Capabilities

### 1. Multi-Document Synthesis

Read multiple documents and synthesize insights:

**Example**: "What are the biggest takeaways from integrations over the past 3 months?"

1. **Parse the question**:
   - Topic: "integrations"
   - Timeframe: "past 3 months" (since ~Oct 2025)
   - Document types: PRDs, RFCs, postmortems (anything relevant)

2. **Find relevant documents**:
   ```bash
   # Find docs about integrations
   grep -r "integration" teams/*/working_docs/ -l

   # Filter by date (created in past 3 months)
   find teams/ -path "*/working_docs/*" -name "*.md" -type f -newer date-ref
   ```

3. **Read documents** (5-10 most relevant):
   - Read full content, not just frontmatter
   - Extract key points, decisions, learnings
   - Note patterns, recurring themes

4. **Synthesize answer**:
   - Identify common themes across docs
   - Extract key takeaways
   - Highlight important learnings or decisions
   - Cite which documents informed the synthesis

5. **Format response** with citations:
   ```
   Based on 7 PRDs and 3 RFCs about integrations from the past 3 months:

   **Key Takeaways:**
   1. Authentication challenges are the #1 issue (mentioned in 6/10 docs)
   2. Rate limiting needs to be built in from day 1 (learned from Widget Inc failure)
   3. Partner success team involvement early reduces post-launch issues by 40%

   **Sources:**
   - Integration PRD for Widget Inc (teams/platform/prds/widget-integration.md)
   - Post-Mortem: Widget Integration Issues (teams/platform/rfcs/widget-postmortem.md)
   - Integration Best Practices RFC (teams/platform/rfcs/integration-best-practices.md)
   - [4 more documents...]

   Want me to go deeper on any of these takeaways?
   ```

---

### 2. Temporal Awareness

Handle time-based queries:

**Timeframe keywords**:
- "over the past [X months/weeks]"
- "recent"
- "in Q[N] [YEAR]"
- "last quarter"
- "since [date/event]"

**Filtering by date**:
```bash
# Get docs created after a certain date
find teams/ -path "*/working_docs/*" -name "*.md" -type f -newermt "2025-10-01"

# Or read frontmatter and filter by created date
grep -h "^created: 2025-" teams/*/working_docs/*/*.md
```

**Temporal synthesis**:
- Group findings by time period
- Show evolution of thinking: "Initially we thought X, but after Y incident, we learned Z"
- Identify trends: "Over the past quarter, 5 of 7 PRDs mention this problem"

---

### 3. Pattern Recognition

Identify patterns across documents:

**Example**: "What mistakes do we keep making?"

1. **Look for keywords**:
   - "lesson learned", "mistake", "issue", "problem", "failure"
   - Postmortem documents
   - "What went wrong" sections in RFCs

2. **Extract patterns**:
   ```bash
   # Find postmortems
   find teams/ -path "*/working_docs/*" -name "*postmortem*.md" -o -name "*post-mortem*.md"

   # Find "lessons learned" sections
   grep -A 10 "lesson" teams/*/working_docs/*/*.md
   ```

3. **Analyze for recurring themes**:
   - Same mistake in multiple docs?
   - Common root causes?
   - Patterns in what goes wrong?

4. **Synthesize**:
   ```
   Based on 8 postmortems and 5 RFCs from 2025:

   **Recurring Mistakes:**
   1. **Underestimating data migration complexity** (4 incidents)
      - Widget Inc integration (Feb)
      - Customer data export (May)
      - Search index rebuild (Aug)

   2. **Insufficient load testing** (3 incidents)
      - API launch (Mar)
      - Batch processing (Jun)

   3. **Missing rollback plans** (2 incidents)
      - Feature flag deployment (Apr)
      - Schema migration (Jul)

   **Pattern**: Most issues (7/8) happened during launches or migrations. Need better pre-launch checklists.
   ```

---

### 4. Learning Extraction

Extract what the team has learned:

**Example**: "What did we learn from the search improvement project?"

1. **Find relevant documents**:
   ```bash
   grep -r "search improvement" teams/ -l
   ```

2. **Read for learnings**:
   - Look for "lessons learned" sections
   - "What worked well" / "What didn't work"
   - Decisions made and their rationale
   - Metrics and outcomes

3. **Synthesize learnings**:
   ```
   From the Search Improvement Project (teams/intelligence/working_docs/prds/search-improvement.md and related docs):

   **What Worked:**
   - Incremental rollout with feature flags (caught issues early)
   - Weekly sync with top 10 customers (great feedback loop)
   - A/B testing every change (proved value before full launch)

   **What Didn't Work:**
   - Initial relevance algorithm was too complex (had to simplify)
   - Underestimated index rebuild time (planned 2 days, took 5)

   **Key Decisions:**
   - Chose Elasticsearch over custom solution (saved 3 months of eng time)
   - Prioritized speed over perfect relevance (users wanted fast results)

   **Outcomes:**
   - Search latency: 800ms → 150ms (81% improvement)
   - User satisfaction: 65% → 89%
   - Adoption: 40% of users now use search daily

   **Lesson**: Incremental rollout + customer feedback loop was critical to success.
   ```

---

### 5. Strategy and Approach Questions

Answer questions about strategy and approach:

**Example**: "What's our approach to AI agents?"

1. **Find strategy documents**:
   ```bash
   grep -r "agent" teams/ -l | grep -E "(rfc|strategy|six-pager)"
   ```

2. **Read for strategic direction**:
   - Goals and objectives
   - Guiding principles/tenets
   - Key decisions
   - Roadmap/phases

3. **Synthesize strategy**:
   ```
   Based on 3 RFCs and 2 six-pagers about AI agents:

   **Our Approach:**
   - **Philosophy**: Agents augment humans, don't replace them
   - **Guiding Principle**: Start narrow and specific, expand over time
   - **Architecture**: Modular, composable agents vs. monolithic

   **Current Focus (Q1 2026)**:
   - Entity resolution agent (in production)
   - Lead enrichment agent (pilot)
   - Research agent (design phase)

   **Key Decisions:**
   - Chose to build on Claude vs. open source models (better quality, faster to market)
   - User-in-the-loop for all agent actions (safety + trust)
   - Agent output is always reviewable and editable

   **Success Criteria:**
   - 80% accuracy on entity resolution
   - 50% time savings for users
   - Zero trust issues (measured by user survey)

   Sources:
   - AI Agent Strategy (teams/intelligence/working_docs/six-pagers/ai-agent-strategy.md)
   - Entity Resolution Agent PRD (teams/intelligence/working_docs/prds/entity-resolution-agent.md)
   - Agent Architecture RFC (teams/platform/working_docs/rfcs/agent-architecture.md)
   ```

---

### 6. Historical Context

Show how thinking has evolved:

**Example**: "How has our thinking evolved on search?"

1. **Find documents over time**:
   ```bash
   # Search-related docs sorted by date
   grep -r "search" teams/ -l | xargs ls -lt
   ```

2. **Read chronologically**:
   - Early docs: what was the initial approach?
   - Middle docs: what changed? Why?
   - Recent docs: what's the current thinking?

3. **Synthesize evolution**:
   ```
   **Evolution of Search Thinking (2023-2026)**:

   **2023: Basic Keyword Search**
   - Initial approach: Simple Elasticsearch keyword matching
   - Why: Fast to implement, good enough for initial launch
   - Limitation: Poor relevance, lots of noise

   **2024: Relevance Improvements**
   - Shift: Added semantic search, relevance scoring
   - Why: Users complained about result quality
   - Learning: Relevance > speed for users

   **2025: Personalization**
   - Shift: User context, team filters, role-based results
   - Why: Users wanted "search that knows me"
   - Learning: Context matters more than we thought

   **2026: AI-Powered**
   - Current: Natural language queries, agent-assisted search
   - Why: Users want answers, not just documents
   - Hypothesis: Search + synthesis = 10x value

   **Pattern**: We've consistently underestimated how much users value relevance and context over speed.
   ```

---

## Process for Synthesis

### Step 1: Parse the Question

Understand what the user is asking for:

**Extract**:
- **Topic**: What subject? (e.g., "integrations", "search", "agents")
- **Timeframe**: When? (e.g., "past 3 months", "Q4 2025", "recent")
- **Document types**: Specific types? (e.g., "PRDs", "postmortems", "RFCs")
- **Teams**: Specific team? (e.g., "intelligence team", "platform team")
- **Question type**:
  - Takeaways/learnings?
  - Strategy/approach?
  - Patterns/mistakes?
  - Historical evolution?
  - Comparison?

---

### Step 2: Find Relevant Documents

Use search to find documents:

```bash
# By topic keyword
grep -r "[topic]" teams/*/working_docs/ -l

# By document type
find teams/ -path "*/working_docs/[type]s/*.md"

# By team
ls teams/[team]/working_docs/[type]s/

# By date
find teams/ -path "*/working_docs/*" -name "*.md" -newermt "[date]"

# Combined
grep -r "[topic]" teams/[team]/working_docs/[type]s/ -l | xargs ls -lt
```

**Prioritize** most relevant documents:
- Exact topic match
- Recent (if timeframe specified)
- Right document type (if specified)
- From right team (if specified)

**Limit** to 5-10 documents (most relevant):
- Reading 10 docs is manageable
- More than 10 becomes overwhelming
- If many matches, prioritize by relevance + recency

---

### Step 3: Read Documents

For each document, read:

1. **Frontmatter** (metadata):
   - Title, type, status, team, owner
   - Created/updated dates
   - Tags, related docs

2. **Content** (full document):
   - Problem statements
   - Solutions and approaches
   - Decisions and rationale
   - Success metrics and outcomes
   - Lessons learned
   - Key points and takeaways

**Extraction** (while reading):
- Take notes on key points relevant to the question
- Note recurring themes across docs
- Identify patterns and connections
- Track which doc each point came from (for citations)

---

### Step 4: Synthesize Answer

**Organize findings**:
- Group related points together
- Identify main themes (2-5 themes)
- Note evidence for each theme (how many docs mention it?)
- Highlight surprises or unexpected patterns

**Structure response**:
```
[Opening: brief context based on what you read]

**[Theme 1 Title]:**
[Synthesis of points]
- Evidence/examples from docs

**[Theme 2 Title]:**
[Synthesis of points]
- Evidence/examples from docs

**[Theme 3 Title]:**
[Synthesis of points]
- Evidence/examples from docs

**[Pattern/Insight]:**
[Higher-level observation across themes]

**Sources:**
- [Doc 1 title] (path)
- [Doc 2 title] (path)
- [Doc 3 title] (path)
- [... list all docs read]

[Closing: offer to go deeper]
```

---

### Step 5: Cite Sources

**Always cite** which documents informed your synthesis:

```
**Sources:**
- Integration PRD for Widget Inc (teams/platform/working_docs/prds/widget-integration.md)
- Post-Mortem: Search Outage (teams/platform/documentation/postmortem-search-outage.md)
- Q4 Strategy Six-Pager (teams/leadership/working_docs/six-pagers/q4-strategy.md)
- [List all documents you read]
```

**Why cite**:
- Transparency: user can verify your synthesis
- Traceability: user can read original docs for more context
- Trust: shows your answer is grounded in real documents

---

### Step 6: Offer to Go Deeper

After answering, offer next steps:

```
Want me to:
- Go deeper on any of these takeaways?
- Read specific documents in detail?
- Compare this to a different time period?
- Look at a related topic?
```

---

## Important Notes

1. **Read the content, not just metadata** - you need to understand what's IN the documents

2. **Limit to 5-10 docs** - reading more becomes unmanageable and overwhelming

3. **Always cite sources** - list every document you read

4. **Synthesize, don't summarize** - find patterns and insights, don't just list what each doc says

5. **Be grounded in evidence** - every claim should be supported by what you read

6. **Temporal awareness** - respect timeframes in the question

7. **No hallucination** - only synthesize from what's actually in the documents

8. **Admit gaps** - if docs don't cover something, say so

9. **Provide clickable paths** - make it easy for user to read source docs

10. **Offer to go deeper** - synthesis is iterative, let users drill down

11. **Pattern recognition** - look for themes across multiple docs

12. **Evolution over time** - show how thinking has changed

---

## Example Interactions

### Example 1: Learnings from Time Period

```
User: "What are the biggest takeaways from integrations over the past three months?"

Agent:
"Let me search for integration-related documents from the past 3 months (since ~Oct 2025)..."

[Searches]:
grep -r "integration" teams/*/working_docs/ -l | xargs ls -lt | head -10

"Found 8 relevant documents: 4 PRDs, 3 RFCs, 1 postmortem. Let me read them..."

[Reads documents - this takes time, shows progress]:
- Reading Widget Inc Integration PRD...
- Reading Integration Framework RFC...
- Reading Postmortem: Widget Inc Issues...
- [... 5 more docs]

[Synthesizes]:

"Based on 8 documents about integrations from the past 3 months:

**Key Takeaways:**

1. **Authentication is the #1 integration challenge** (mentioned in 6/8 docs)
   - OAuth2 flows are complex and error-prone
   - Partners often have non-standard implementations
   - Solution: Build reusable auth library (now in platform RFC)

2. **Rate limiting needs to be built in from day 1** (learned from Widget Inc failure)
   - Widget Inc integration crashed their API (no rate limits on our side)
   - Cost us 2 weeks and damaged relationship
   - New standard: All integrations MUST include rate limiting + backoff

3. **Partner success involvement early reduces post-launch issues by ~40%**
   - Integrations with early partner success involvement: 2 issues avg
   - Integrations without: 7 issues avg
   - New process: Partner success in design phase, not just launch

4. **Webhook reliability is harder than expected**
   - 3/4 integrations had webhook delivery issues
   - Partners don't always have retry logic
   - Solution: We need webhook queue + retry on our side

**Pattern**: Most issues (6/8) were preventable with better upfront design. We're now creating an Integration Playbook to capture these learnings.

**Sources:**
- Integration PRD for Widget Inc (teams/platform/working_docs/prds/widget-integration-2025-003.md)
- Post-Mortem: Widget Integration Issues (teams/platform/documentation/postmortem-widget-integration.md)
- Integration Framework RFC (teams/platform/working_docs/rfcs/integration-framework-2025-012.md)
- Salesforce Integration PRD (teams/platform/working_docs/prds/salesforce-integration-2025-004.md)
- HubSpot Integration PRD (teams/platform/working_docs/prds/hubspot-integration-2025-005.md)
- Webhook Reliability RFC (teams/platform/working_docs/rfcs/webhook-reliability-2025-015.md)
- Integration Best Practices One-Pager (teams/platform/working_docs/one-pagers/integration-best-practices-2025-002.md)
- Integration Playbook Six-Pager (teams/platform/working_docs/six-pagers/integration-playbook-2025-001.md)

Want me to go deeper on any of these takeaways?"
```

### Example 2: Strategy Question

```
User: "What's our strategy for Q2 based on recent RFCs?"

Agent:
"Let me find RFCs from Q1 2026 (Jan-Mar) that discuss Q2 plans..."

[Searches]:
find teams/ -path "*/working_docs/rfcs/*.md" -newermt "2026-01-01"

"Found 5 RFCs from Q1 2026. Reading..."

[Reads]:
- Q2 Planning RFC...
- Platform Investment RFC...
- AI Agent Expansion RFC...
- [2 more]

[Synthesizes]:

"Based on 5 RFCs from Q1 2026:

**Q2 2026 Strategy:**

1. **Platform Investment Focus**
   - Goal: Build foundations for scale
   - Key initiatives:
     - API rate limiting and quotas
     - Webhook infrastructure
     - Integration framework
   - Why: Q1 taught us poor infrastructure causes incidents

2. **AI Agent Expansion**
   - Goal: 3 agents in production (up from 1)
   - Agents:
     - Entity resolution (already live)
     - Lead enrichment (new - Q2 launch)
     - Research agent (new - Q2 beta)
   - Why: Entity resolution showing 60% time savings

3. **Enterprise Customer Focus**
   - Goal: 5 enterprise deals closed
   - Requirements:
     - SSO (blocker for 3 current deals)
     - SCIM provisioning
     - Advanced permissions
   - Why: Enterprise ARR is 3x SMB, need to unlock this segment

4. **Technical Debt Paydown**
   - Goal: 20% of eng time on tech debt
   - Priorities:
     - Search index migration (blocking perf improvements)
     - Database sharding (hitting limits)
     - Test coverage (currently 45%, target 70%)
   - Why: Slowing down shipping velocity

**Key Tradeoff**: Balancing new features (agents, enterprise) vs. foundations (platform, tech debt). Decision: 60% features, 40% foundations.

**Success Metrics**:
- 3 agents live (measurable)
- 5 enterprise deals (measurable)
- Search p95 latency < 200ms (measurable)
- Eng satisfaction with codebase >7/10 (team survey)

**Sources:**
- Q2 Planning RFC (teams/leadership/working_docs/rfcs/q2-planning-2026.md)
- Platform Investment Strategy (teams/platform/working_docs/rfcs/platform-investment-2026.md)
- AI Agent Expansion RFC (teams/intelligence/working_docs/rfcs/agent-expansion-2026.md)
- Enterprise Requirements RFC (teams/platform/working_docs/rfcs/enterprise-requirements-2026.md)
- Tech Debt Reduction Plan (teams/platform/working_docs/rfcs/tech-debt-q2-2026.md)

Want to drill into any specific area?"
```

### Example 3: Pattern Recognition

```
User: "What mistakes do we keep making with launches?"

Agent:
"Let me search for postmortems and 'lessons learned' sections in RFCs..."

[Searches]:
find teams/ -name "*postmortem*.md" -o -name "*post-mortem*.md"
grep -r "lesson" teams/*/working_docs/ -l

"Found 6 postmortems and 8 docs with 'lessons learned' sections from 2025. Reading..."

[Reads all 14 documents]

[Synthesizes]:

"Based on 6 postmortems and 8 RFCs with launch retrospectives from 2025:

**Recurring Launch Mistakes:**

1. **Insufficient load testing (5 incidents)**
   - API Launch (Mar): 10x actual traffic, site down 2 hours
   - Batch processing (Jun): Memory issues with large datasets
   - Search reindex (Aug): Brought down DB with too many queries
   - Agent launch (Oct): Rate-limited partner APIs
   - Export feature (Dec): Overwhelmed queue system
   - **Pattern**: We test with small/medium data, then launch hits real scale

2. **Missing/untested rollback plans (4 incidents)**
   - Feature flag deployment (Apr): Couldn't disable without redeploy
   - Schema migration (Jul): No easy rollback, had to restore backup
   - Config change (Sep): Rolled forward to fix instead of back
   - Agent update (Nov): Rollback broke dependencies
   - **Pattern**: We have rollback plans on paper, but don't test them

3. **Underestimating data migration complexity (3 incidents)**
   - Widget integration (Feb): 5 days vs planned 1 day
   - Customer data export (May): Data quality issues caused delays
   - Search reindex (Aug): Edge cases not in test data
   - **Pattern**: Real data is messier than test data

4. **Inadequate monitoring/alerting (3 incidents)**
   - Discovered issues from customer reports, not monitoring
   - Alerts too noisy (ignored) or too quiet (missed issues)
   - **Pattern**: Monitoring is added after incident, not before

5. **Communication gaps (2 incidents)**
   - Sales team didn't know about downtime (angry customers)
   - Support team not briefed on new feature (couldn't help users)
   - **Pattern**: Eng launches without looping in other teams

**Root Cause Pattern**:
Most mistakes (11/14) stem from **insufficient pre-launch validation**:
- Testing doesn't match production scale/data
- Rollback plans exist but aren't validated
- Monitoring added reactively, not proactively

**What's Improved in Q4**:
- Launch checklist now mandatory (includes load testing, rollback test)
- Staging environment now has prod-scale data subset
- Support/sales briefing now part of launch process

**What Still Needs Work**:
- Load testing at true prod scale (expensive/complex)
- Chaos engineering (test rollback regularly)
- Pre-launch war games (simulate things going wrong)

**Sources:**
[Lists all 14 documents with paths]

Want me to dig into any specific mistake pattern?"
```

---

## Reading vs. Listing

**Search & Synthesis reads documents**. This is different from search skill, which lists documents.

**Example of reading**:
```bash
# Search & Synthesis reads full content
cat teams/intelligence/working_docs/prds/entity-resolution.md

# Extracts key information
- Problem: Manual entity matching takes 5 hours/week per user
- Solution: AI agent that suggests matches with 85% accuracy
- Success metric: 80% time savings
- Key decision: Chose Claude over open-source (quality > cost)
- Learning: Users want confidence scores, not just matches
```

**Example of listing (search skill)**:
```bash
# Search lists documents
ls teams/intelligence/working_docs/prds/
- entity-resolution.md
- gtmbench-v1.md
- lead-enrichment.md
```

**Key difference**:
- **Search**: "Here are the documents about X"
- **Search & Synthesis**: "Based on reading the documents about X, here's what we learned..."
