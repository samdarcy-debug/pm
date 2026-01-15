---
id: weekly-context-engineering-2025-36
title: "Context Engineering Weekly Report - September 06, 2025"
type: weekly-report
status: approved
team: context-engineering
owner:
created: 2025-09-06
updated: 2026-01-06
week_ending: 2025-09-06
reporting_period: "September 2-6, 2025"
tags: ["weekly-report", "Q32025"]
---

# **Context Engineering Team Executive Roundup - September 5, 2025**

## **Executive Summary**

The Context Engineering team has achieved critical alignment on the MCP
(Model Context Protocol) server architecture for signals data, with
Srivatsa securing executive sponsorship from Ryan Stevens and a clear
path to production by mid-September. The team faces a strategic
inflection point around data granularity - Robyn\'s discovery that
ZoomInfo lacks business unit-level resolution for enterprise accounts
(e.g., Disney vs Disney+) threatens competitive parity in lookalike
recommendations and requires immediate data team investment. With the
October 14th Dreamforce announcement looming, the team needs decisive
action on resource allocation and MCP orchestration strategy to avoid
tool conflicts at scale.

## **This Week\'s Progress**

### **Key Momentum Areas**

Srivatsa achieved breakthrough consensus on MCP server design,
finalizing the approach to group 30+ signals into consumable tools via
the go-to-market store, with Vinod providing hands-on implementation
guidance Monday. This unlocks the critical path for exposing ZoomInfo\'s
intelligence layer as context services, directly feeding into the
October 14th launch alongside Dreamforce.

Robyn\'s lookalike accounts proposal gained executive acceptance,
positioning the team to validate SMB market fit next week through
targeted seller interviews across multiple verticals. The 40-cent data
credit pricing model provides the economic framework needed to scale
AI/ML features while maintaining margin integrity.

Christine\'s data audit initiative is converging toward completion
today, establishing the foundational understanding of ontologies and
schema relationships necessary for proper MCP tool integration. Her
insights on APS score visibility beyond the feed represent
forward-thinking product evolution as we transition to agent-first
interfaces.

### **Goals & Progress**

**MCP Server Development**: Srivatsa has mapped the complete
signal-to-tool architecture and secured stakeholder alignment with
Punkaj\'s team. The decision to leverage go-to-market store data
positions us within the broader MCP ecosystem, enabling shared benefits
from platform improvements. Meeting with Vinod Monday provides the
technical pathway to have a functional server within 10 days. 85%
complete on design, 0% on implementation.

**Algorithm Validation & Testing**: Robyn is executing comparative
analysis of the new APS algorithm against ZI Labs baselines for three
target customers, while simultaneously establishing the testing
framework for lookalike recommendations. The SMB seller interviews next
week will validate whether our strategic advantage in mid-market
translates to user value. Contact metrics finalization enables revenue
attribution. 60% complete on setup, validation begins next week.

**Data Architecture Documentation**: Christine\'s data audit draft
completion today establishes the knowledge base for cross-functional
alignment on data structures. Her proactive self-education on ontologies
and schema through Claude demonstrates the leverage possible when PMs
deeply understand our technical foundation. Initial draft 90% complete,
iterations to follow.

### **Strategic Challenges**

The enterprise data granularity gap Robyn identified poses immediate
competitive risk - without business unit resolution, our lookalike
recommendations fail to match competitor precision for Fortune 500
accounts. This impacts not just lookalikes but cascades through APS,
FIT, and IMS scoring at product level. Root cause analysis reveals
ZoomInfo\'s historical account-centric model conflicts with modern
product-level go-to-market motions. We need executive commitment to
systematic business unit mapping starting with top enterprise accounts.

Resource allocation for MCP server implementation remains unresolved
despite Monday\'s guidance session with Vinod. George\'s takeover from
Ryan Franceschi creates transition friction just as we need
acceleration. Rowan\'s suggestion to piggyback on existing servers
offers a pragmatic workaround - we could deploy signals tools on
Vinod\'s infrastructure as proof-of-concept rather than waiting for
dedicated resources. This requires immediate decision to maintain
October timeline.

MCP tool orchestration complexity emerges as our blind spot - Robyn
correctly identifies that without a \"deciding agent\" architecture,
multiple teams building MCPs independently will create tool conflicts
and unpredictable agent behavior. Each new tool potentially introduces
confusion to the orchestrator about when to call signals versus scores
versus recommendations. This requires immediate cross-team coordination
and testing framework before we hit production scale.

## 

## 

## **Strategic Insights**

### **Key Learnings & Discoveries**

Christine\'s observation about APS score exposure beyond the feed
reveals a critical product evolution opportunity - as we deprecate feeds
for agent-first experiences, real-time score calculation on company
profile pages becomes essential. This shifts our architecture from
batch-processed stack ranking to on-demand scoring, reducing
computational overhead while improving user experience. This insight
should influence how we design all scoring mechanisms going forward.

Robyn\'s discovery that the 40,000+ SKU complexity at companies like
Cisco and Oracle requires user-level definition rather than data-level
resolution fundamentally changes our approach to personalization.
Instead of trying to map every product relationship, we let individual
sellers define their context through the user profile, making the
impossible merely difficult. This user-driven taxonomy could become our
differentiation against competitors stuck in rigid hierarchies.

The team\'s convergence on go-to-market store as the data foundation for
MCP tools, rather than ZDP, represents strategic alignment with the
broader platform direction. Srivatsa and Majid\'s namespace design
(all-signals directory plus individual signal namespaces) provides
elegant orchestration for agents to discover and consume capabilities.
This positions us within the ecosystem momentum rather than building in
isolation.

### **Cross-Team Dependencies**

Our work with Bernard\'s team on MCP tools for semantic data integration
continues to be critical for the October 14th announcement. Rowan\'s
direct experience building these integrations provides valuable
guidance, but we need formal coordination mechanisms to prevent tool
proliferation and naming conflicts. The \"small selection of
purpose-built, battle-hardened tools\" approach for launch requires
aggressive scope management.

The data team\'s involvement becomes mission-critical for the business
unit mapping initiative. Robyn and Rowan\'s aligned perspective that
enterprise account granularity unlocks differentiated value across
recommendations, competitive intelligence, and messaging requires
immediate escalation to data team leadership. Christine\'s suggestion to
leverage 10-K business unit reporting structures offers a scalable
starting point for this mapping exercise.

##  

## **Looking Ahead**

Next week centers on MCP server implementation velocity following
Monday\'s session with Vinod, with the critical decision on whether to
build dedicated infrastructure or leverage existing servers determining
our October 14th readiness.

Robyn\'s SMB seller interviews will validate lookalike algorithm
performance across verticals while establishing the feedback loop
necessary for rapid iteration. Success looks like clear signal on which
verticals show strong product-market fit and which require algorithm
adjustments. The parallel APS comparison with ZI Labs will quantify our
competitive position. These validation cycles directly inform what we
can credibly announce at Dreamforce.

The team must also crystallize the MCP orchestration strategy to prevent
tool conflicts as multiple teams contribute capabilities. This requires
documented standards for tool naming, parameter design, and interaction
patterns. Without this governance framework, our October launch risks
delivering a confused agent experience that damages credibility. The
path forward demands both technical excellence in individual components
and systemic thinking about their interaction at scale.

*Source: Team 1-2-3 Operating Framework entries from September 2-6,
2025*
