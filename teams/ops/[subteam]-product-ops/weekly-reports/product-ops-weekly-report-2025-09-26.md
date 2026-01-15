---
id: weekly-product-ops-2025-39
title: "Product Ops Weekly Report - September 26, 2025"
type: weekly-report
status: approved
team: product-ops
owner:
created: 2025-09-26
updated: 2026-01-06
week_ending: 2025-09-26
reporting_period: "September 22-26, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Product Ops Team Executive Roundup - September 22-26, 2025**

## **Executive Summary**

Product Ops achieved a breakthrough in platform integration this week,
with Sam Darcy securing access to the MCP server that enables full
backend-to-frontend tool deployment through ZI Chat. This unlocks the
complete foundation needed to rapidly deploy Voice of Customer tools and
knowledge graph capabilities directly into the platform. The team
delivered three major system completions: Brett Jacobs finalized the
Copilot Workspace talk track agent ahead of the October 6th launch, Ken
Elwell created a functional marketing content agent, and Daniel Kong
streamlined the Knowledge Center buildout process from a month-long
effort to 1-2 weeks.

## **This Week\'s Progress**

### **Key Momentum Areas**

Sam Darcy secured direct access to ZI Chat\'s MCP server from Zheng
Zhong, creating the complete end-to-end infrastructure needed for agent
deployment. This breakthrough means the team can now add custom agents
to the MCP server and have them immediately available in ZI Chat,
eliminating the previous backend limitations that required workarounds.

Brett Jacobs completed the Copilot Workspace talk track agent after
multiple iterations, incorporating the demo from Ant. The solution is
now ready for trainer rollout, with Laser and Lou being trained today,
followed by full CX and sales organization training next week ahead of
the October 6th product launch.

Daniel Kong redesigned the Knowledge Center buildout process,
transforming it from the 25-step individual PM workflow used for GTM
Studio into a streamlined 2-3 step batch review process. This reduces PM
workload while maintaining quality, with agent-assisted article writing
replacing manual documentation tasks.

### **Goals & Progress**

**Platform Infrastructure**: Sam Darcy achieved the core breakthrough by
gaining MCP server access, completing the missing piece needed for full
agent deployment. The Voice of Customer tool now has robust transcript
search capabilities ready for ZI Chat integration, with additional
agents in development for the MCP pipeline.

**GTM Copilot Launch Readiness**: Brett Jacobs delivered the finalized
talk track agent with integrated demo capabilities. Ken Elwell
established FAQ update processes to prevent knowledge graph and talk
track systems from providing outdated information to the GTM team during
the critical launch period.

**Knowledge Management Systems**: Ken Elwell created a functional
marketing content agent that successfully mimics knowledge graph
capabilities as a proof of concept. Daniel Kong accelerated Knowledge
Center development for Copilot Workspace, working with Sean Walter and
the CX team to implement the new batch processing approach.

**Release Process Optimization**: Kristin Gandini documented and secured
TPM team buy-in for the off-cycle release process, specifically
addressing GTM Studio and Copilot Workspace releases. The documentation
has been shared with enablement and integrated into existing dashboards
and automations.

### **Strategic Challenges**

The marketing content agent created by Ken Elwell, while functional,
quickly exposes scalability limitations without the full knowledge graph
infrastructure. The team identified this creates an opportunity to
demonstrate exactly what the knowledge graph should accomplish, but also
adds urgency to secure Neo4J deployment approval from infrastructure
teams.

Resource management for the marketing content agent requires immediate
attention, as Brett Jacobs noted the tool essentially opened Product Ops
services to the entire marketing organization without sustainable
support processes. The team needs to establish feedback channels and
update cadences with support from Katie and Jesse to prevent becoming
reactive product support for marketing requests.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Ken Elwell\'s work on the marketing content agent revealed fundamental
architecture insights about LLM knowledge integration. Direct document
referencing in prompts fails at scale, particularly when documents
aren\'t structured for LLM ingestion, while summarizing content into
structured source documents essentially creates inferior versions of
knowledge graphs. This validates the team\'s knowledge graph approach
and provides clear technical justification for the architecture
decisions.

Daniel Kong\'s Knowledge Center process redesign demonstrates
significant efficiency gains through batch processing and agent
assistance. By requiring PMs to provide document dumps rather than
individual feature definitions, the team reduced coordination complexity
while enabling agents to handle the heavy lifting of article creation,
leaving PMs with simple review tasks.

Brett Jacobs identified that the team\'s evolution toward product
management mindsets is essential for managing the increasing feedback
volume and stakeholder opinions. Taking ownership of products rather
than being service providers allows the team to evaluate feedback
critically and maintain focus on strategic objectives rather than
drowning in reactive requests.

### **Cross-Team Dependencies**

The Neo4J licensing and deployment decision remains the single most
important dependency for scaling knowledge graph capabilities. Sam Darcy
is reconnecting with Pond College, Andrew Harris, and Andy Weiss to
accelerate this approval process, with Brett Jacobs committed to pushing
it through if needed.

Jack\'s team can begin LaunchDarkly tool development earlier than
anticipated, creating opportunities for enhanced PM workflow automation
beyond the primary CX transparency use case. Kristin Gandini is
coordinating on data requirements and integration scope to maximize this
accelerated timeline.

## **Looking Ahead**

Next week focuses on operationalizing this week\'s breakthroughs, with
Sam Darcy leading MCP server integration to get Voice of Customer tools
live in ZI Chat. The team will also establish sustainable processes for
the marketing content agent to prevent reactive support cycles.

The October 6th Copilot Workspace launch represents the culmination of
multiple workstreams, with final FAQ updates by Sean Walter and
knowledge base preparation by Daniel Kong. Ken Elwell will coordinate
with Daniel Kong on process alignment and swimlanes to ensure accurate
information flows through all GTM tools during the launch period.

Brett Jacobs will prioritize developing sustainable management processes
for the marketing content agent with support from Katie and Jesse, while
Sam Darcy drives Neo4J deployment approval to unlock full knowledge
graph capabilities. The convergence of Voice of Customer tools,
knowledge graph infrastructure, and agent deployment capabilities
positions the team to deliver significant value acceleration in the
coming weeks.

*Source: Team 1-2-3 Operating Framework entries from September 22-26,
2025*
