# **Product Management Knowledge Repository**

👋 **New here?** Read this README first to understand what this is, then:

1. Install and open Claude Code (\[installation instructions \- (https://discoverorg.atlassian.net/wiki/spaces/IE/pages/202450272570/Users+-+How+to+use+requesty.ai+in+Claude+Code+-+2.0.75)\])  
2. Say: **"Clone the PM repository"** (Claude Code will handle this for you)  
3. Say: **"Onboard me"** (\~1 minute to get set up)

Welcome to the product organization knowledge repository. This is a Git-based knowledge management system that centralizes all product knowledge and insights across teams. Using the power of Claude Code, you can create documents, answer questions, and access institutional knowledge in a systematic, AI-powered way.

---

## **What This Is & Why It Exists**

**The Problem**: Product knowledge is scattered across Google Docs, Slack threads, and people's heads. Finding past decisions, understanding what we've learned, and avoiding repeated mistakes is nearly impossible.

**The Solution**: A centralized "product org brain" that contains all context and knowledge across teams \- past decisions, learnings, customer insights, best practices, and institutional knowledge in one searchable place.

**What Makes This Different**: This isn't just a document repository. Claude Code acts as an intelligent oracle that knows YOUR organization specifically:

* Ask "What do we know about integrations?" and get answers from YOUR past work and learnings  
* Create a PRD and Claude references relevant past decisions, personas, and constraints from YOUR org  
* The system gets smarter over time as you add more knowledge \- it learns from every document

**Key Capabilities**:

* Create documents informed by your organization's accumulated knowledge  
* Answer questions using context from across all teams  
* Surface relevant past work and learnings automatically  
* Find domain experts and document owners instantly

This is made possible by Claude Code's ability to traverse the entire repository, understand relationships between documents, and synthesize information across your entire product organization.

---

## **How It Works**

### **The PR-Based Working Documents Model**

**Main branch \= source of truth**

* Everything in main is considered "official" documentation  
* Claude Code uses this as the authoritative source for answering questions and creating documents  
* High bar for what gets merged \- this maintains the quality of the "brain"

**Local copy \= your scratch space**

* Clone the repo to work on documents locally  
* Experiment, iterate, and create without constraints  
* Your private workspace for thinking and drafting

**Pull requests \= collaborative working space AND changelog**

* All changes go through PRs to track feedback, iterations, and decisions  
* Creates a clear audit trail of what changed and why  
* Enables structured collaboration with inline comments  
* Multiple rounds of review happen within the PR thread

### **Team Organization**

**Structure**:

* DAI-level team folders (top level)  
* Sub-team folders within each DAI team  
* Teams organize their folders however they want (by project, doc type, person, etc.)

**What goes in your team folder**:

* Team documents (PRDs, RFCs, one-pagers, six-pagers)  
* Sources of truth (product documentation, technical specs)  
* Team best practices and learnings  
* Research and customer insights  
* Synthesized decisions from meetings  
* Anything that helps Claude Code understand your team's context

### **Permissions & Control**

* **Full control over your team's folder**: Manage your own content and structure  
* **Team member approvals**: Any team member can approve PRs for their team folder  
* **Global folders**: Skills and cross-team content require Product Ops admin approval  
* **No self-approvals**: All changes require review from another person

---

## **Getting Started: Your User Journey**

### **Initial Setup (One-Time)**

**1\. Install Claude Code**

* \[Installation instructions \- (https://discoverorg.atlassian.net/wiki/spaces/IE/pages/202450272570/Users+-+How+to+use+requesty.ai+in+Claude+Code+-+2.0.75)\]

**2\. Clone the repository**

* Open Claude Code  
* Say: "Clone the PM repository"  
* Claude Code will handle the cloning for you

**3\. Run the onboarding skill**

* Say: "Onboard me"  
* This will:  
  * Create your person profile  
  * Set up GitHub CLI for creating PRs  
  * Configure git hooks  
  * Get you ready to work

### **Daily Workflow**

**1\. Work locally**: Create and iterate on documents in your cloned repo

* Your local copy is your scratch space  
* Experiment and draft without constraints

**2\. Get feedback**: When ready, create a PR and assign reviewers

* This creates a new branch for collaboration  
* Designate who should review your work

**3\. Iterate in PR**: Comments, suggestions, and revisions happen in the PR

* Reviewers leave inline comments on specific sections  
* You push updates to the same branch as you refine  
* Multiple rounds of review are expected and normal

**4\. Merge to main**: Once approved, merge becomes official documentation

* Now part of the source of truth  
* Claude Code will use this for future work  
* Be careful what you approve \- maintain quality standards

**5\. Use Claude Code**: Ask questions, create docs, all informed by the repo

* "Create a PRD for \[feature\]" \- guided document creation  
* "What do we know about \[topic\]?" \- search across all team knowledge  
* "Have we tried this before?" \- surface relevant past work  
* "Create a PR for review" \- initiate feedback process

---

## **Repository Structure**

```
/
├── _templates/              # Document templates
├── teams/
│   ├── [team-name]/
│   │   ├── _people/         # Required: team member profiles
│   │   ├── [subteam-name]/  # Sub-team folders
│   │   └── [your-org]/      # Organize as you see fit
│   └── ...
└── skills/                  # Global skills (Product Ops managed)
```

**Notes**:

* Only `_people/` folder is required in each team directory  
* Beyond that, organize your team folder however works best for you  
* Common patterns: folders by project, document type (prds/, rfcs/), or person

---

## **Appendix**

### **A. Permissions & CODEOWNERS**

The repository uses an auto-generated CODEOWNERS system:

* Creating a person profile automatically makes you a code owner for your team's folder  
* Your GitHub username is auto-inferred from your filename  
* CODEOWNERS regenerates automatically when person profiles change

**Approval rules**:

* **Team folders**: Any team member can approve PRs that only touch their team's content  
* **Global folders**: Only Product Ops admins can approve  
* **Cross-team PRs**: Require approval from at least one affected team's code owner  
* **No self-approvals**: All PRs require review from another person

### **B. What Are Skills?**

Skills are pre-built workflows for common tasks that work through Claude Code. They guide you through structured processes with the right questions and formatting.

**Location**:

* Global skills live in `skills/` (managed by Product Ops)

**How to use**:

* Just talk to Claude Code naturally: "Onboard me", "Create a PRD", etc.  
* Skills trigger automatically based on your request  
* They guide you through the right questions and create properly structured documents

**Examples**:

* Onboarding \- creates your person profile and sets you up  
* PRD creation \- walks through building a product requirements document  
* Document search \- finds relevant past work across the repository

### **C. How Product Search Works**

Claude Code understands your repository through:

**YAML Frontmatter**:

* Every document has structured metadata (owner, team, status, tags)  
* This makes documents discoverable and queryable  
* Claude uses this to understand relationships and context

**Person Files**:

* Your person profile establishes your identity in the system  
* Documents link to people as owners, stakeholders, reviewers  
* Enables finding domain experts: "Who knows about X?"

**Tags and Metadata**:

* Consistent tagging makes content discoverable  
* Use lowercase, hyphenated slugs (e.g., `entity-resolution`, `q1-2025`)  
* Tags enable queries like "Show me all Q1 initiatives"

**Document Linking**:

* Link to other documents and people using wiki-link syntax  
* Claude can traverse these relationships to answer questions  
* Makes the knowledge graph explorable

### **D. Best Practices**

**Do**:

* **Use Claude Code for everything** \- it handles frontmatter fields, updating documents, descriptive commit messages, and proper formatting automatically  
* Keep your person profile up to date  
* Link to other documents and people liberally  
* Create PRs when you need feedback

**Don't**:

* Merge PRs without proper review

---

## **Getting Help**

* **Questions about this system?** Ask in \#product-ops  
* **Found a bug or want a feature?** File an issue in this repository  
* **Need help with a specific document?** Tag the document owner or your team lead
