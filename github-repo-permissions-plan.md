# **GitHub Repository Permissions & Workflow Plan**

## **Repository Structure**

### **Folder Hierarchy Decision**

**Final approach:** Team-based folders with nested working docs and
documentation folders

/team-name/

/working-docs/

/documentation/

/subfolder-1/

/subfolder-2/

/weekly-reports/

**Key rationale:**

- AI semantic search works regardless of folder structure (it\'s
  indexed)

- Team folders provide better human experience for finding related
  documentation

- Working docs are private to the team; documentation is for broader
  consumption

- Teams maintain their own folder structures as they evolve

### **Example: Product Ops Structure**

****/ops/

/people/ (permissions folder containing all ops team members: BI, PMM,
Product Ops)

/bi/

/working-docs/

/documentation/

/weekly-reports/

/pmm/

/working-docs/

/documentation/

/weekly-reports/

/product-ops/

/working-docs/

/documentation/

/early-access/

/mcr/

/voc/

/operating-model/

/weekly-reports/

## **Permissions System**

### **People Docs**

**Purpose:** Grant folder-level access to team members

**Location:** One people folder per top-level team (e.g., /ops/people/)

**How it works:**

1.  During onboarding, users run the onboard skill to set up their
    people doc

2.  Users specify their team association (e.g., \"context engineering
    team\")

3.  This association determines default folder placement for all their
    documents

4.  Each user has exactly ONE people.md file in ONE folder (their
    primary team folder)

**Key decisions:**

- **Permissions are NOT set at subteam folder level** - too complex to
  manage

- People docs are placed at the DAI (top-level team) level

- Each user only has one people.md file, even if they need access to
  multiple folders

### **Team Assignment Rules**

**Standard team members:**

- Associated with one primary team folder

- Default document location = their team\'s working-docs folder

**DAIs (Directors/Leaders):**

- People doc goes in their DAI folder (e.g., AJ in /ops/, Victor in
  /gtm-workspace/)

- Default document location = their DAI team\'s working-docs folder

- DAIs are made admin/code owners to grant access to both:

  - Their own DAI folder

  - The leadership folder

- This is the ONLY reason someone would need access to multiple team
  folders

- Each DAI still only has ONE people.md file in their primary DAI folder
  (not in leadership)

## **Document Workflows**

**Critical Decision: All changes require PR process**

- At the end of the discussion, you decided everything should go through
  PR workflow

- Even admins cannot bypass (uncheck \"allow bypass by admin\" setting)

- Admins can self-approve, but must still create PR

- Brett set default behavior to create PR, not direct commit

### **Standard Workflow (All Documents)**

**Process:**

1.  Create document in working-docs folder (or upload from Google Docs)

2.  When ready, create a PR

3.  Designate specific reviewers

4.  Reviewers provide feedback via PR comments or \@mentions

5.  Author makes edits based on feedback (in same PR)

6.  Once approved, document is finalized

**For simple documentation (like Dominic\'s memos):**

- Still requires PR, but can be self-approved quickly if you have
  permissions

- \"Just take the memo and put it\... Boom\" - but through PR process

**Still being determined:**

- Whether approved PR automatically moves doc from working-docs to
  documentation

- OR if user must move doc to documentation before creating PR

- Preference is for automatic movement after approval, but technical
  feasibility unclear

### **PR Approval Rights**

**Current setup:**

- Admins can approve any PR

- Team members can approve PRs only within their team folder

- Branch protection requires PR approval before merging to main

**Questions to resolve:**

- How to handle cross-team collaboration (someone outside the team
  providing input)

- Distinction between \"collaboration/comments\" vs. \"final approval\"

- Whether non-team-members can be designated as reviewers

## **Technical Configuration**

### **Branch Protection**

- **Require PR for all changes** (even from admins)

- Admins can self-approve but must follow PR process

- Default behavior: Create PR, not direct commit

- Option to \"allow bypass by admin\" can be disabled to enforce PR
  workflow universally

### **CODEOWNERS**

**Current state:**

- Grants PR approval rights within team folders

- Any team member with rights in their folder can approve PRs there

- Admins have universal approval rights

**Needs clarification:**

- Can external reviewers be designated on a per-PR basis?

- How to configure reviewer requirements (number needed, specific
  people, etc.)

## **Open Questions & Next Steps**

### **Technical Questions**

1.  Can approved PRs automatically move docs from working-docs to
    documentation?

2.  Can non-team-members be designated as reviewers on specific PRs?

3.  **How does self-approval work in GitHub?** You discussed that admins
    \"can auto-approve ourselves anyway\" but weren\'t sure where the
    self-approval button is or if the \"require approval before
    merging\" setting allows self-approvals

4.  How to allow collaboration/comments without granting approval
    rights?

### **Process Questions**

1.  Should users specify documentation subfolder during PR creation?

2.  How to handle documents that span multiple teams?

3.  What\'s the process for reorganizing documentation over time?

### **Immediate Tasks (Daniel)**

- Update people doc system to include subteam association

- Set default folder based on team association

- Create workflow documentation for end users

- Continue working on CODEOWNERS configuration

- Test and validate PR workflows

- Build out automated flows for the document workflow

- Ensure semantic search is functioning reliably

- Test with Product Ops team, Adam Severance\'s team, and DAIs

### **Success Criteria**

- PMs can use the system without explanation

- Document review process feels natural (like code review)

- AI search returns accurate, relevant results

- Minimal manual intervention required for common workflows
