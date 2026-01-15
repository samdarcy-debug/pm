---
id: weekly-product-ops-2025-41
title: "Product Ops Weekly Report - October 10, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-10-10
updated: 2026-01-06
week_ending: 2025-10-10
reporting_period: "October 6-10, 2025"
tags: ["weekly-report", "Q42025"]
---

# **Product Ops Team Executive Roundup - October 6-10, 2025**

## **Executive Summary**

The team made progress this week with Sam Darcy integrating the Voice of
Customer tool with the microapp chatbot for easier access and
integration with other tools in chat. Simultaneously, Ken Elwell and
Daniel Kong made significant progress on the Copilot Workspace content
creation system, building out the end-to-end process and agent that will
allow product marketers and enablement teams to self-serve content
without repeatedly pulling PMs away from building. The team is ready to
begin rollout to PMs next week, though we\'ve identified that the
knowledge graph\'s traversal logic needs refinement after initial
testing showed the simpler agent outperforming the graph-based approach.
Caleb Munson has begun structuring the annual planning process with
fresh eyes, creating clearer documentation and identifying where we\'ve
historically struggled with execution follow-through rather than initial
strategy setting.

## **This Week\'s Progress**

### **Key Momentum Areas**

Ken Elwell created a working Copilot Workspace content agent that
successfully produced a sales talk track matching our actual output,
requiring zero prompting beyond specifying the asset type. This
validates the core concept and demonstrates that the system can work
with the right inputs. Ken built the agent using three foundational
documents that serve as lightweight knowledge graphs: positioning and
framing, product capabilities, and competitive landscape. This proves
the viability of the approach before scaling to the more complex graph
structure.

Daniel Kong built out the complete process for updating the product
knowledge base, working through real examples rather than theory to
expose gaps in how knowledge creators would actually use the system. He
secured alignment from Katie and AJ to proceed with the rollout, and has
the agents ready to refresh and prune the knowledge base. Daniel\'s work
on the knowledge creator side of the system complements Ken\'s content
generation work, creating the full loop of how product information flows
into usable assets.

Sam Darcy integrated the Voice of Customer tool with the microapp
chatbot, making it accessible within chat for easier integration with
other tools. This initial version provides the foundation for continued
iteration on data quality and feature development.

### **Goals & Progress**

**Copilot Workspace Launch Infrastructure**: The team is positioned to
roll out the content creation system to PMs next week, starting with a
meeting with Victor\'s team on Tuesday. Ken, Daniel, and Brett have
aligned on the knowledge creator workflow and are finalizing the content
creator rollout strategy, deciding whether to launch broadly or test
with a smaller group first. The system will serve as a pilot for
understanding how teams will contribute to and extract value from a
knowledge graph at scale, informing the longer-term architecture.

**Knowledge Graph Development**: Initial testing revealed that the first
knowledge graph implementation produced weaker outputs than the simpler
agent approach, which Ken expected given it was the very first test. The
team identified three potential causes for the performance gap: document
quality, system prompt configuration, or traversal logic. Brett and Sam
both believe the traversal mechanism is the key differentiator and
likely culprit, as the default graph traversal from the graffiti library
may not be sufficient for this use case. The challenge is that Sam needs
to focus on VOC work and can only serve as an advisor rather than an
implementer on the knowledge graph refinement.

**Annual Planning Process Design**: Caleb Munson reviewed all past
annual planning documentation and created a high-level process overview
with clearer definitions of commonly used terms, addressing what he
observed as \"inside baseball\" documentation that assumed too much
context. He synthesized the five different names teams had used for the
same planning artifacts and established consistent nomenclature. Brett
acknowledged that past planning cycles were \"average at best\" due to
bandwidth constraints, noting the team has historically done well with
initial strategy setting and the director-level planning responses, but
has never developed strong execution and adjustment processes after
plans are set. Caleb plans to kick off the next cycle mid-November with
an eight-week timeline, though he flagged concern about layering this
heavy lift onto the existing \"mad scramble\" of Q4 milestones.

### **Strategic Challenges**

The knowledge graph work faces a resource constraint that could slow
progress at a moment when momentum matters. Sam\'s expertise in building
the advanced traversal logic would be valuable, but he\'s rightfully
focused on the VOC tool work that Dominik is requesting. Ken could
experiment with implementing traversal improvements on a branch using
the old knowledge graph code as reference, but there\'s risk of breaking
existing functionality or getting confused by deprecated concepts. The
team needs to decide whether to accept slower iteration on the knowledge
graph enhancement or find another path forward that doesn\'t depend on
Sam as an implementer.

Rolling out the Copilot Workspace system requires coordinating with
launch operations team members who need to review and help administer
the new process. Brett identified this as a blocker, noting the system
is ready from a technical standpoint but needs operational buy-in and
support infrastructure. The broader question is how to scale this across
content creators beyond the initial pilot, balancing the desire to move
quickly with the need to ensure teams understand how to use the system
effectively.

Caleb raised a pattern he\'s observing after his first month: there are
frequent discussions across teams about plans, dependencies, and what
each team is doing. He\'s uncertain whether this represents healthy
continuous planning where teams don\'t wait 90 days to adjust course, or
whether it signals insufficient context-setting that leaves people
unclear on their priorities. This ambiguity matters as the team designs
the next planning cycle, particularly the balance between providing rich
strategic context upfront versus enabling lightweight ongoing
adjustments. Brett noted this deserves deeper exploration when Kristin
Gandini returns.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Ken\'s testing revealed that taking a real use case and building it live
accelerates learning dramatically compared to theoretical planning. The
Copilot Workspace example forced the team to work through actual
workflows and edge cases, making it clear what documentation structure
is needed and where gaps exist. Brett echoed this insight, noting the
team keeps relearning that jumping into live use cases is the fastest
path to clarity, though the thinking often circles back to the same
conclusions. The implication is to default to rapid prototyping with
real scenarios rather than extensive upfront design.

Daniel\'s experience walking through a single example end-to-end exposed
how much more comprehensive the process documentation needs to be beyond
just explaining how the system works technically. Users need clear
guidance on when to update information, what format to use, how to
handle edge cases, and how to verify their contributions were processed
correctly. This suggests the team should build process scaffolding
alongside any new tools rather than treating it as a later addition.

The first knowledge graph test provides valuable signal despite poor
results. The team hypothesizes that product marketing use cases may need
explicit top-down framing built into the knowledge graph to guide
navigation, rather than relying on the agent to discover relevant
connections through general traversal. This would be a significant
architectural insight if validated, suggesting different use cases may
require different graph structures or navigation strategies.

### **Cross-Team Dependencies**

Our rollout of the Copilot Workspace system depends on coordination with
Katie and the launch operations team to review processes and determine
how to administer the new workflow. Brett is working to establish
clearer collaboration between PMs and customer experience teams during
the release process, specifically getting CX to engage earlier on
customer impact rather than consuming information only when releases are
final. This connects to the broader MCR improvements and represents a
shift toward AI-first release coordination that could reduce last-minute
scrambles.

Sam\'s VOC work includes a specific request from Dominik for next week.
Guy and Dominik have been identified as potential resources for helping
remove blockers on VOC infrastructure and deployment needs.

## **Looking Ahead**

Next week centers on executing the Copilot Workspace rollout while
beginning to gather real-world feedback on both the content creation
process and the underlying knowledge management approach. The team will
shift from building to learning mode, watching how PMs actually interact
with the system and where friction appears.

Ken, Daniel, and Brett will facilitate the rollout to Victor\'s PM team
on Tuesday, with particular attention to the knowledge creator workflow
where PMs update product information. This first wave of users will
reveal whether the process documentation is clear enough and whether the
agents successfully maintain knowledge base quality. Simultaneously, the
team needs to finalize the content creator rollout strategy, determining
whether to bring in all marketing and enablement team members at once or
start with a smaller test group. Success here means proving that
non-experts can generate high-quality assets without PM involvement,
freeing product teams to focus on building. Sam will dedicate time to
the VOC data quality improvements Dominik requested while continuing to
bring the microapp version to feature parity with the original custom
tool. Caleb will engage Sarah Herritage in the annual planning feedback
process and begin scoping a change management plan that acknowledges the
organization\'s limited capacity for simultaneous changes.

The team has built significant momentum across multiple fronts this
week, validating core technical approaches while identifying the
specific areas that need refinement. The shift to real-world testing
next week will determine how well the theoretical designs hold up under
actual use and inform the next iteration of both the Copilot Workspace
system and the broader knowledge graph strategy.

*Source: Team 1-2-3 Operating Framework entries from October 6-10, 2025*
