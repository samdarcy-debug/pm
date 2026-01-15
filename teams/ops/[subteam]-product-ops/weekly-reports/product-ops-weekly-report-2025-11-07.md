---
id: weekly-product-ops-2025-45
title: "Product Ops Weekly Report - November 07, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-11-07
updated: 2026-01-06
week_ending: 2025-11-07
reporting_period: "November 3-7, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Product Ops Executive Roundup - November 3, 2025**

## **Executive Summary**

Frustrating week as the team encountered major data & infrastructure
blockers this week that delayed the planned VOC tool rollout, automated
release details, and analyzing Studio/Workspace calls so far, though
viable solutions are now in hand and testing resumes this afternoon.
Despite these setbacks, the team shipped some tangible wins: Kristin
Gandini launched two major capabilities - the agentic platform
prototyping tool for the organization and the automated tech
documentation tool for the CX team using Github PRs and Jira ticket
info, both now in active use. Ken Elwell had promising success running
personalized release communication at scale through GTM Studio and
Workspace, though some product gaps to work through. The week showcased
the reality of building new things - unexpected technical challenges
alongside concrete progress.

## **This Week\'s Progress**

### **Key Momentum Areas**

**Agentic Platform Prototyping Launch**: Kristin Gandini successfully
launched the agentic platform prototyping tool to the organization,
enabling PMs to build and prototype their own agents using whatever
tools, artifacts, and prompts they want, then incorporate these directly
into prototypes. The tool creates an unexpected benefit by using the
real agentic platform, naturally injecting real data into prototypes and
making them more realistic for planning purposes.

**CX Team Tech Documentation Automation**: Kristin Gandini launched the
automated tech documentation tool with the CX team enablement group, who
are now running with it independently. This marks the second production
deployment this week of tools that directly benefit end stakeholders,
demonstrating increasing operational maturity in delivering finished
capabilities.

**GTM Studio Personalized Releases Success**: Ken Elwell successfully
ran personalized releases through GTM Studio and Workspace,
demonstrating the first working example of pushing information directly
to the GTM team without middlemen. The workflow enables identifying
which releases are most relevant to specific accounts and why, then
delivering that context directly to where sellers execute. A few product
gaps emerged during testing that need attention, but the core
functionality works well and will be tested with CSMs next week.

### **Goals & Progress**

**VOC Tool Infrastructure Resolution**: Brett Jacobs encountered major
timeouts between the agentic platform and chatbot that blocked the
planned VOC tool rollout. Sam Darcy spent the week addressing networking
restrictions in the stack given the non-standard architecture with
microapp front end, agentic layer, and MCP server for tool calls. As of
this morning, a fix is available and being implemented. Sam is pushing
out a workaround version this afternoon that uses the API to generate
the fragments and entities needed, then imports results into the
microapp, enabling testing to proceed while the permanent networking fix
deploys.

**Pitch Talk Track Analysis Framework**: Ken Elwell developed the
three-part framework for analyzing pitch effectiveness: identifying
which calls pitched Studio or Workspace and getting call IDs, gathering
full transcripts for those calls since summaries won\'t capture specific
rep language, and analyzing the transcripts at scale. Russell is working
on unblocking the most challenging part - identifying relevant calls at
scale - with an update expected Sunday. BigQuery provides a viable path
for transcript retrieval once call IDs are identified.

**Automated Release Information Data Blockers**: Daniel Kong sent out
communications and aligned stakeholders on responsibilities for the
product knowledge system rollout, including quick phone calls with Randy
and the TPM team to resolve initial confusion. The focus shifted to
automated product release information, but Daniel hit blockers on the
data side. This work relates to Kristin Gandini\'s tech release
automation tool that uses GitHub PRs and Jira ticket information, where
Kristin worked with technical support people to establish the data flow.
Daniel needs to see the actual data from Dan\'s team but faces
permission access issues - when downloads do work, files sometimes
contain only null values, making it impossible to determine what\'s
possible to create.

**VOC Workflow Proposal Development**: Kristin Gandini shared a proposal
for an ongoing VOC workflow focused on top customer feedback and
continued building out the top-down report capabilities. Token limit
challenges persist in ZI Chat when using large system prompts, but the
core workflow structure for collecting Jira tickets and enabling deeper
investigation into specific feedback areas is mapped out and ready for
testing once infrastructure limitations are resolved.

### **Strategic Challenges**

**Data Access Dependencies Blocking Product Release Automation**: Daniel
Kong remains blocked waiting to see data from Dan\'s team before being
able to design the automated product release information system.
Permission access issues prevent downloading needed data, and when
downloads do work, the files sometimes lack the necessary information.
The time zone and weekend differences with the offshore team require
quick morning feedback rounds to maintain progress, but without seeing
the actual data structure and content, it\'s difficult to determine
what\'s possible to create and how to integrate into existing workflows.

**Token Limit Constraints in VOC Agents**: Kristin Gandini continues
hitting token limits in ZI Chat when trying to run agents with large
system prompts and CSV data for the top-down VOC report workflow. The
system prompt is too large even before adding any actual analysis data.
Brett Jacobs suggested workarounds including splitting datasets by theme
and filtering CSV data to remove uncategorized fragments (about 30% of
content), but this requires engagement with the chat team to find a
sustainable solution that maintains analytical depth.

**Pitch Call Identification at Scale**: Ken Elwell faces the challenge
of identifying which calls discussed GTM Studio and Copilot Workspace at
scale to enable pitch effectiveness analysis. While transcript gathering
and analysis appear tractable once call IDs are available, determining
which calls are relevant from the full corpus is proving harder than
expected. Russell\'s analysis will determine whether the semantic
pipeline or Chorus API provides a viable path, with the complication
that semantic data contains fragments rather than full transcripts,
potentially requiring reconstruction of complete conversations.

## **Strategic Insights**

### **Key Learnings & Discoveries**

**Direct GTM Enablement Opportunity**: Ken Elwell discovered this is the
first time he has actually needed to use ZoomInfo products rather than
just looking around at them, revealing a valuable opportunity. The GTM
Studio to Workspace flow creates a direct channel to push information to
the GTM team without middlemen, enabling Product Ops to leverage deep
release knowledge to identify relevant account implications and deliver
actionable context directly where sellers execute.

**Agentic Platform Prototyping Side Benefits**: Kristin Gandini found
that the agentic platform prototyping tools create a valuable side
benefit beyond their primary purpose. Because they use the real agentic
platform, they naturally inject real data into prototypes, making them
more realistic for planning purposes. This bridges a long-standing gap
where prototypes often felt artificial and disconnected from actual
system capabilities.

**Communication Mode Effectiveness**: Daniel Kong validated that
aligning via quick calls is much more effective than sending long
messages via Slack, though sometimes both are necessary. The phone
conversations with Randy and the TPM team quickly resolved confusion
that written communications had created, establishing clear role
boundaries and workflow expectations that might have taken multiple
message rounds to achieve.

**Infrastructure Complexity Reality**: Brett Jacobs articulated the
learning that many things that seem like they should be easy turn out to
be hard, citing examples like identifying calls that discussed specific
products or resolving timing and gateway issues. The team lacks clear
patterns for solving these types of problems, making it difficult to
estimate effort or identify when to escalate versus persist. This
uncertainty complicates planning and creates frustration when
straightforward-seeming work reveals hidden complexity.

### **Cross-Team Dependencies**

Russell\'s work on identifying relevant pitch calls will be sent Sunday,
providing the foundation for Ken Elwell\'s talk track analysis work. The
approach Russell develops for this problem will likely inform similar
use cases requiring selective call identification from large
conversation datasets.

Dan\'s team controls access to the product release data that Daniel Kong
needs to build the automated release information system. The permission
and data format issues are blocking progress on a system with
substantial downstream value for both Product Ops and the broader
organization.

The chat team\'s involvement will be necessary to resolve Kristin
Gandini\'s token limit issues, as current workarounds degrade the user
experience and analytical capability. The CSV size and system prompt
length are both contributing factors that need architectural solutions
beyond individual optimizations.

## **Looking Ahead**

Next week focuses on recovering momentum after this week\'s
infrastructure setbacks while pushing forward on multiple workstreams
that are now unblocked or have clear paths forward.

**VOC Tool Testing and Deployment**: Brett Jacobs and Kristin Gandini
will test the VOC extension this afternoon once the front end is ready,
with Brett needing to leave at 2:30 to pick up Elise. Despite expecting
to encounter more issues based on this week\'s experience, there is high
confidence that the underlying functionality works well and the
remaining challenges center on deployment and user interface refinements
rather than fundamental design problems. Sam Darcy\'s workaround enables
testing to proceed before the permanent networking fix is in place.

**CSM Testing of Personalized Releases**: Ken Elwell plans to test the
personalized release flow with actual CSMs next week, building on this
week\'s successful run-through of the GTM Studio to Workspace
functionality. The test will use a real CSM (likely Zach Day, who has
been discussing AI capabilities with Ken) to validate whether
personalized account summaries can effectively reach reps and be
actionable in their territory planning. The few product gaps identified
this week need attention, but the core capability is proven and ready
for real-world validation.

**Product Release Automation Data Acquisition**: Daniel Kong will focus
intensively on the product release automation work, needing to see the
actual data and figure out what is possible to create and how to bring
it into existing workflows. The goal for next week is having knowledge
bases updated with automated release information, including replicating
Joggin\'s newsletter automation. Kristin Gandini will also work on
bridging the gap between automated weekly releases and the LRT piece, as
this backtracking is becoming increasingly necessary given Mary\'s
feedback.

**Top-Down VOC Report Rollout**: Brett Jacobs will begin rolling out the
top-down report workflow while continuing to refine the VOC tool based
on testing results. Kristin Gandini will focus on ensuring the workflow
can stand up whenever the tool is fully ready, and will spend time
investigating how to enable PMs to use VOC for further discovery beyond
the tactical execution focus of the top-down report. The real value
multiplier comes from setting up infrastructure that PMs can use
independently, similar to Klein, rather than from one-off report
generation.

The team demonstrated resilience this week by identifying workarounds
for major blockers while still shipping two production capabilities. The
focus on unblocking dependencies and validating real world workflows
positions next week for significant progress across multiple
initiatives, with clearer understanding of both technical constraints
and user needs informing the path forward.

*Source: Team Operating Document Friday Reflection entries and team
meeting transcript from November 3, 2025*
