---
id: weekly-mcp-2025-46
title: "MCP Weekly Report - November 14, 2025"
type: weekly-report
status: approved
team: mcp
owner:
created: 2025-11-14
updated: 2026-01-06
week_ending: 2025-11-14
reporting_period: "November 10-14, 2025"
tags: ["weekly-report", "Q42025"]
---

# **MCP Tiger Team Executive Roundup - November 14th, 2025**

## **Executive Summary**

The team made substantial progress on MCP infrastructure fundamentals
this week, with Topher delivering control plane functionality for server
creation and Carter advancing the config server implementation. However,
a security flagging issue with the ChatGPT connector has emerged as the
primary blocker---OpenAI\'s systems are marking our integration as
unsafe, and their lack of diagnostic visibility makes troubleshooting
extremely difficult. We\'re pursuing both executive channels through
Dominik and direct support routes, while Anthropic has granted us beta
access to programmatic tool calling and tool search features that
warrant near-term exploration.

## **This Week\'s Progress**

### **Key Momentum Areas**

Topher shipped control plane capabilities that enable dynamic MCP server
management, including create/update operations, live version
registration during server initialization, and a role/tag authorization
system that properly filters tool access. This infrastructure unlocks
the ability to programmatically manage our growing tool ecosystem rather
than relying on manual configuration.

Carter deployed the config server shell to staging and established the
foundation for passing map configuration into the gateway. While DevOps
dependencies remain (GCS bucket creation and pub/sub topic setup), the
service architecture is now in place and ready for self-service tooling
once the infrastructure pieces land.

Zheng successfully tested the complete MCP flow with ZoomInfo\'s chatbot
using the new gateway subdomain, validating that our core oauth2 works
end-to-end. This proof point confirms our architectural approach even as
we work through connector-specific challenges.

### **Goals & Progress**

**MCP Infrastructure Build-out**: The control plane now supports full
CRUD operations for MCP servers along with scope management separated
from API scopes. Carter's config server is staged pending infrastructure
provisioning (GCS bucket and pub/sub topic) from DevOps. The team
expects Pat to deliver the required secrets and pub/sub setup, though
the bucket creation depends on backstage service registration completing
first.

**Third-Party Orchestration**: Zheng validated the ZoomInfo chatbot
integration pattern successfully, but ChatGPT integration remains
blocked by OpenAI\'s security scanning. The team is pursuing multiple
remediation paths including potential contact escalation through
Dominik\'s channels and direct developer account troubleshooting. The
lack of diagnostic information from OpenAI makes systematic debugging
impossible.

**Combined Tool Exploration**: Rowan initiated design work for tool
aggregation patterns---combining related tools like \"lookup accounts\"
and \"enrich accounts\" into unified interfaces that reduce choice
complexity for LLMs. The team will hold a requirements session Monday to
establish acceptance criteria for this work.

### **Strategic Challenges**

OpenAI\'s ChatGPT connector is flagging our integration as unsafe with
no diagnostic details about which specific elements triggered their
security scan. We\'ve tried removing semantic data from descriptions
without resolution, suggesting the issue may be broader in OpenAI\'s
evaluation criteria. Rowan is exploring two parallel paths: leveraging
Dominik\'s OpenAI contacts for direct technical escalation, and opening
a developer support account to attempt standard troubleshooting
channels. The challenge is compounded by OpenAI\'s forum-based support
showing no concrete solutions for similar issues, and their apparent
current focus on consumer rather than enterprise use cases despite
maintaining robust enterprise connector documentation.

Carter has clear dependencies on DevOps infrastructure (GCS bucket
creation, pub/sub topic configuration) that gate config server
completion. While Pat is working on the secrets, the bucket requires
backstage self-service tooling to work against the service that just
deployed to staging. These infrastructure blockers are manageable but
create sequencing constraints on delivery timing.

The team is resource-constrained for the scope of active work
streams---building the gateway, exposing third-party orchestration,
maintaining existing integrations, and now incorporating experimental
work on new Anthropic capabilities. Rowan explicitly called out that the
team needs dedicated time for pattern exploration and architecture
validation alongside delivery commitments, particularly as the major LLM
providers introduce new capabilities that could significantly improve
our implementation approach.

## **Strategic Insights**

### **Key Learnings & Discoveries**

Anthropic granted beta access to two capabilities that change our
architectural calculus: programmatic tool calling and a built-in tool
search function. The tool search feature is particularly relevant since
we were planning to build similar functionality to handle tool discovery
at scale. This suggests we should validate Anthropic\'s implementation
pattern before building custom solutions---either adopting their
approach directly or learning from their design to improve our own
architecture. The timing is advantageous as we\'re still in active build
phase rather than refactoring production code.

Tool visibility and selection is emerging as a strategic battleground
beyond pure technical implementation. As Rowan noted, we\'re entering an
era of \"agent attention\"---when orchestrators connect to dozens of
potential tools, how do individual tools get selected and used? This has
direct financial implications as companies implement credit charging for
tool execution. Organizations that optimize for LLM attention and
selection likelihood will generate more revenue, creating incentives for
potentially adversarial behavior in tool metadata and descriptions.

The team validated that marking tools as \"searchable\" in MCP involves
setting default loading to true, which means external orchestrators like
Claude will load tools like HubSpot before performing tool search
operations. This raises questions about whether we should implement tool
search logic server-side within our gateway rather than client-side in
the MCP server pattern, giving us more control over tool discovery and
presentation ordering.

### **Cross-Team Dependencies**

DevOps needs to deliver GCS bucket creation and pub/sub topic
configuration to unblock Topher\'s config server work. Pat is currently
handling the secrets management portion. The self-service backstage
tooling requires the service to exist first, which Carter deployed to
staging this morning, so the dependency chain should resolve early next
week.

Rowan is coordinating with Dominik on potential OpenAI contact
escalation for the ChatGPT security issue. The team needs either
diagnostic information about what\'s triggering the safety flags or a
direct technical contact who can provide implementation guidance, as
public forums show no viable solutions for similar connector blocking
issues.

## **Looking Ahead**

Next week the team continues core infrastructure delivery---Carter
completing config server once DevOps dependencies land, then shifting to
request routing and control plane support. Topher advances tool tagging
and request routing capabilities while requiring API key creation
support (already in progress with Pat). Zheng persists on ChatGPT
connector resolution through both support channels and technical
experimentation.

Monday\'s combined tool meeting will establish acceptance criteria for
the tool aggregation pattern, which addresses LLM choice complexity by
consolidating related operations into unified interfaces. This pattern
work runs parallel to the potential MCP team office hours call where we
can probe best practices, resource/prompt template support plans, and
their roadmap for features that affect our architecture decisions.

The team faces a fundamental tension between delivery velocity and
architectural validation. The new Anthropic capabilities (programmatic
tool calling, tool search) warrant hands-on exploration before we lock
in implementation patterns, yet the existing ticket backlog already
exceeds current team capacity. Rowan will raise this resourcing and
prioritization question in today\'s gateway API meeting with Dominik and
Filip---we need explicit guidance on how to balance experimentation time
against sprint commitments when the experimentation could fundamentally
improve our long-term architecture.
